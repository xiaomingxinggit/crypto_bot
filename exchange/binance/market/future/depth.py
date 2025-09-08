# exchange/binance/market/future/depth.py
from exchange.binance.api.api import Future
from utils.http_client import http_client
from exchange.binance.model.future import FutureDepth
from typing import Union, Dict, Any

class FutureDepthService:
    """
    币安永续合约订单簿深度接口封装（服务类）
    返回 model 定义的 FutureDepth 实体类
    """

    def __init__(self):
        self.client = http_client

    def get_depth(self, symbol: str, limit: int = 100) -> Union[FutureDepth, None]:
        """
        获取订单簿深度
        :param symbol: 交易对
        :param limit: 深度条数 (5, 10, 20, 50, 100, 500, 1000, 5000)
        :return: FutureDepth 对象 或 None
        """
        params = {"symbol": symbol, "limit": limit}
        data = self.client.get(Future.DEPTH, params=params)
        if not data:
            return None

        try:
            # 将 API 返回的 bids 和 asks 转换为 FutureDepth 对象
            bids = [[price, qty] for price, qty in data["bids"]]
            asks = [[price, qty] for price, qty in data["asks"]]
            return FutureDepth(bids=bids, asks=asks)
        except KeyError as e:
            print(f"❌ 数据字段缺失: {e}")
            return None