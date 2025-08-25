# exchange/binance/market/spot/price.py
from exchange.binance.api.api import Spot
from utils.http_client import http_client
from typing import Union, Dict, Any

class SpotPrice:
    """
    币安现货价格接口封装
    """

    def __init__(self):
        self.client = http_client

    def get_price(self, symbol: str = None) -> Union[Dict[str, Any], list, None]:
        """获取最新价格"""
        params = {"symbol": symbol} if symbol else {}
        return self.client.get(Spot.TICKER_PRICE, params=params)

    def get_24hr_ticker(self, symbol: str = None) -> Union[Dict[str, Any], list, None]:
        """获取24小时行情"""
        params = {"symbol": symbol} if symbol else {}
        return self.client.get(Spot.TICKER_24HR, params=params)

    def get_avg_price(self, symbol: str) -> Union[Dict[str, Any], None]:
        """获取加权平均价"""
        if not symbol:
            raise ValueError("symbol is required")
        return self.client.get(Spot.AVG_PRICE, params={"symbol": symbol})

    def get_best_ticker(self, symbol: str = None) -> Union[Dict[str, Any], list, None]:
        """获取最优挂单"""
        params = {"symbol": symbol} if symbol else {}
        return self.client.get(Spot.BEST_TICK, params=params)

    def get_all_book_tickers(self) -> Union[list, None]:
        """获取所有最优挂单"""
        return self.client.get(Spot.ALL_BOOK_TICKS)