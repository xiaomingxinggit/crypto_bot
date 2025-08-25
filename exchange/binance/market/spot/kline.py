# exchange/binance/market/spot/kline.py
from exchange.binance.api.api import Spot
from utils.http_client import http_client
from typing import Union, List, Any

class SpotKline:
    """
    币安现货K线数据接口封装
    """

    def __init__(self):
        self.client = http_client

    def get_klines(self, symbol: str, interval: str, limit: int = 500,
                   start_time: int = None, end_time: int = None) -> Union[List[Any], None]:
        """
        获取K线数据
        :param symbol: 交易对
        :param interval: 时间周期 (1m, 5m, 1h, 1d 等)
        :param limit: 返回条数 (1-1000)
        :param start_time: 开始时间戳 (ms)
        :param end_time: 结束时间戳 (ms)
        """
        params = {"symbol": symbol, "interval": interval, "limit": limit}
        if start_time:
            params["startTime"] = start_time
        if end_time:
            params["endTime"] = end_time
        return self.client.get(Spot.KLINE, params=params)

    def get_uiklines(self, symbol: str, interval: str, limit: int = 500,
                     start_time: int = None, end_time: int = None) -> Union[List[Any], None]:
        """
        获取前端优化K线数据 (与klines返回相同)
        """
        params = {"symbol": symbol, "interval": interval, "limit": limit}
        if start_time:
            params["startTime"] = start_time
        if end_time:
            params["endTime"] = end_time
        return self.client.get(Spot.UIKLINES, params=params)