# exchange/binance/market/future/exchange_info.py
from exchange.binance.api.api import Future
from utils.http_client import http_client
from typing import Union, Dict, Any

class FutureExchangeInfo:
    """
    币安永续合约交易对信息接口封装
    """

    def __init__(self):
        self.client = http_client

    def get_exchange_info(self, symbol: str = None) -> Union[Dict[str, Any], None]:
        """获取合约交易规则和交易对信息"""
        params = {"symbol": symbol} if symbol else {}
        return self.client.get(Future.EXCHANGE_INFO, params=params)