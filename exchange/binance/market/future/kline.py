# exchange/binance/market/future/kline.py
from exchange.binance.api.api import Future
from utils.http_client import http_client
from typing import Union, List, Any

class FutureKline:
    """
    币安永续合约K线数据接口封装
    """

    def __init__(self):
        self.client = http_client

    def get_klines(self, symbol: str, interval: str, limit: int = 500,
                   start_time: int = None, end_time: int = None) -> Union[List[Any], None]:
        """获取K线数据"""
        params = {"symbol": symbol, "interval": interval, "limit": limit}
        if start_time:
            params["startTime"] = start_time
        if end_time:
            params["endTime"] = end_time
        return self.client.get(Future.KLINE, params=params)

    def get_continuous_klines(self, pair: str, contract_type: str, interval: str, limit: int = 500,
                              start_time: int = None, end_time: int = None) -> Union[List[Any], None]:
        """获取连续合约K线数据"""
        params = {"pair": pair, "contractType": contract_type, "interval": interval, "limit": limit}
        if start_time:
            params["startTime"] = start_time
        if end_time:
            params["endTime"] = end_time
        return self.client.get(Future.CONTINUOUS_KLINE, params=params)

    def get_index_klines(self, pair: str, interval: str, limit: int = 500,
                         start_time: int = None, end_time: int = None) -> Union[List[Any], None]:
        """获取价格指数K线数据"""
        params = {"pair": pair, "interval": interval, "limit": limit}
        if start_time:
            params["startTime"] = start_time
        if end_time:
            params["endTime"] = end_time
        return self.client.get(Future.INDEX_KLINE, params=params)

    def get_mark_price_klines(self, symbol: str, interval: str, limit: int = 500,
                              start_time: int = None, end_time: int = None) -> Union[List[Any], None]:
        """获取标记价格K线数据"""
        params = {"symbol": symbol, "interval": interval, "limit": limit}
        if start_time:
            params["startTime"] = start_time
        if end_time:
            params["endTime"] = end_time
        return self.client.get(Future.MARK_PRICE_KLINE, params=params)

    def get_premium_index_klines(self, symbol: str, interval: str, limit: int = 500,
                                 start_time: int = None, end_time: int = None) -> Union[List[Any], None]:
        """获取溢价指数K线数据"""
        params = {"symbol": symbol, "interval": interval, "limit": limit}
        if start_time:
            params["startTime"] = start_time
        if end_time:
            params["endTime"] = end_time
        return self.client.get(Future.PREMIUM_INDEX_KLINE, params=params)