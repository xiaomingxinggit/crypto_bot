# utils/http_client.py
import requests
import time
from typing import Any, Dict, Optional
from utils.logger import logger

# 默认配置
DEFAULT_TIMEOUT = 10
MAX_RETRIES = 3
RETRY_DELAY = 1.0
BACKOFF_FACTOR = 1.5


class HttpClient:
    """
    通用 HTTP 客户端，用于 crypto_bot 项目
    """

    def __init__(self, base_url: str = "", timeout: int = DEFAULT_TIMEOUT, max_retries: int = MAX_RETRIES):
        self.base_url = base_url.rstrip("/")
        self.timeout = timeout
        self.max_retries = max_retries
        self.session = requests.Session()

    def _build_url(self, url: str) -> str:
        if url.startswith("http://") or url.startswith("https://"):
            return url
        return f"{self.base_url}/{url.lstrip('/')}" if self.base_url else url

    def _log_request(self, method: str, url: str, **kwargs):
        params = kwargs.get("params")
        json_data = kwargs.get("json")
        data = kwargs.get("data")

        logger.debug(f"📤 {method} {url}")
        if params:
            logger.debug(f"  🔍 Params: {params}")
        if json_data:
            logger.debug(f"  📦 JSON: {json_data}")
        if data:
            logger.debug(f"  📥 Data: {data}")

    def _log_response(self, method: str, url: str, response: requests.Response):
        duration = response.elapsed.total_seconds()
        status = response.status_code
        if status < 400:
            logger.debug(f"📥 {method} {url} → {status} ({duration:.2f}s)")
        else:
            logger.warning(f"⚠️  {method} {url} → {status} ({duration:.2f}s)")

    def request(self, method: str, url: str, **kwargs) -> Optional[Dict[str, Any]]:
        method = method.upper()
        url = self._build_url(url)
        last_exception = None

        kwargs.setdefault("timeout", self.timeout)

        for attempt in range(self.max_retries + 1):
            try:
                self._log_request(method, url, **kwargs)
                response = self.session.request(method=method, url=url, **kwargs)
                self._log_response(method, url, response)

                if response.status_code < 400:
                    try:
                        return response.json()
                    except Exception as e:
                        logger.warning(f"⚠️ 无法解析 JSON 响应: {e}")
                        return {"raw": response.text}

                if response.status_code < 500:
                    logger.error(f"❌ {method} {url} → {response.status_code}: {response.text}")
                    return None
                else:
                    logger.warning(f"🔁 服务端错误 {response.status_code}，准备重试...")

            except requests.exceptions.Timeout:
                logger.error(f"❌ 请求超时: {url}")
                last_exception = "Timeout"
            except requests.exceptions.ConnectionError as e:
                logger.error(f"❌ 连接失败: {url} | {e}")
                last_exception = "ConnectionError"
            except requests.exceptions.RequestException as e:
                logger.error(f"❌ 请求异常: {e}")
                last_exception = str(e)

            if attempt < self.max_retries:
                delay = RETRY_DELAY * (BACKOFF_FACTOR ** attempt)
                time.sleep(delay)
                logger.warning(f"🔄 重试 {attempt + 1}/{self.max_retries} → {url}")
            else:
                logger.error(f"🛑 达到最大重试次数，请求失败: {url}")
                if last_exception:
                    logger.error(f"最后一次错误: {last_exception}")

        return None

    def get(self, url: str, **kwargs) -> Optional[Dict[str, Any]]:
        return self.request("GET", url, **kwargs)

    def post(self, url: str, **kwargs) -> Optional[Dict[str, Any]]:
        return self.request("POST", url, **kwargs)

    def put(self, url: str, **kwargs) -> Optional[Dict[str, Any]]:
        return self.request("PUT", url, **kwargs)

    def delete(self, url: str, **kwargs) -> Optional[Dict[str, Any]]:
        return self.request("DELETE", url, **kwargs)


# ====================
# 全局 HTTP 客户端实例
# ====================
http_client = HttpClient(timeout=10, max_retries=3)