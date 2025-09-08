# exchange/binance/market/future/exchange_info.py
from exchange.binance.api.api import Future
from utils.http_client import http_client
from exchange.binance.model.future import FutureExchangeInfo
from typing import Union, Dict, Any

class FutureExchangeInfoService:
    """
    币安永续合约交易对信息接口封装（服务类）
    返回 model 定义的 FutureExchangeInfo 实体类
    """

    def __init__(self):
        self.client = http_client

    def get_exchange_info(self, symbol: str = None) -> Union[FutureExchangeInfo, None]:
        """
        获取合约交易规则和交易对信息
        :param symbol: 交易对（可选）
        :return: FutureExchangeInfo 对象 或 None
        """
        params = {"symbol": symbol} if symbol else {}

        data = self.client.get(Future.EXCHANGE_INFO, params=params)
        if not data:
            return None

        try:
            return FutureExchangeInfo(
                timezone=data["timezone"],
                serverTime=data["serverTime"],
                rateLimits=data["rateLimits"],
                exchangeFilters=data["exchangeFilters"],
                symbols=data["symbols"]
            )
        except KeyError as e:
            print(f"❌ 数据字段缺失: {e}")
            return None