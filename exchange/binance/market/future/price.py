# exchange/binance/market/future/price.py
from exchange.binance.api.api import Future
from utils.http_client import http_client
from typing import Union, Dict, Any

class FuturePrice:
    """
    币安永续合约价格接口封装
    """

    def __init__(self):
        self.client = http_client

    def get_price(self, symbol: str = None) -> Union[Dict[str, Any], list, None]:
        """获取最新价格"""
        params = {"symbol": symbol} if symbol else {}
        return self.client.get(Future.TICKER_PRICE_V2, params=params)

    def get_24hr_ticker(self, symbol: str = None) -> Union[Dict[str, Any], list, None]:
        """获取24小时行情"""
        params = {"symbol": symbol} if symbol else {}
        return self.client.get(Future.TICKER_24HR, params=params)

    def get_mark_price(self, symbol: str = None) -> Union[Dict[str, Any], list, None]:
        """获取标记价格和资金费率"""
        params = {"symbol": symbol} if symbol else {}
        return self.client.get(Future.LATEST_MARK_PRICE, params=params)

    def get_funding_rate(self, symbol: str, limit: int = 100) -> Union[Dict[str, Any], list, None]:
        """获取资金费率历史"""
        params = {"symbol": symbol, "limit": limit}
        return self.client.get(Future.FUNDING_RATE_HISTORY, params=params)

    def get_best_ticker(self, symbol: str = None) -> Union[Dict[str, Any], list, None]:
        """获取最优挂单"""
        params = {"symbol": symbol} if symbol else {}
        return self.client.get(Future.BEST_TICK, params=params)