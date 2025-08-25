# exchange/binance/market/spot/exchange_info.py
from exchange.binance.api.api import Spot
from utils.http_client import http_client
from typing import Union, Dict, Any

class SpotExchangeInfo:
    """
    币安现货交易对信息接口封装
    """

    def __init__(self):
        self.client = http_client

    def get_exchange_info(self, symbol: str = None) -> Union[Dict[str, Any], None]:
        """获取交易规则和交易对信息"""
        params = {"symbol": symbol} if symbol else {}
        return self.client.get(Spot.EXCHANGE_INFO, params=params)