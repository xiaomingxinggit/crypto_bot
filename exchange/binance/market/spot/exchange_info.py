# exchange/binance/market/spot/exchange_info.py
from exchange.binance.api.api import Spot
from utils.http_client import http_client
from exchange.binance.model.spot import SpotExchangeInfo
from typing import Union, Dict, Any

class SpotExchangeInfoService:
    """
    币安现货交易对信息接口封装（服务类）
    返回 model 定义的 SpotExchangeInfo 实体类
    """

    def __init__(self):
        self.client = http_client

    def get_exchange_info(self, symbol: str = None) -> Union[SpotExchangeInfo, None]:
        """
        获取交易规则和交易对信息
        :param symbol: 交易对（可选）
        :return: SpotExchangeInfo 对象 或 None
        """
        params = {"symbol": symbol} if symbol else {}

        data = self.client.get(Spot.EXCHANGE_INFO, params=params)
        if not data:
            return None

        try:
            return SpotExchangeInfo(
                timezone=data["timezone"],
                serverTime=data["serverTime"],
                rateLimits=data["rateLimits"],
                exchangeFilters=data["exchangeFilters"],
                symbols=data["symbols"]
            )
        except KeyError as e:
            print(f"❌ 数据字段缺失: {e}")
            return None