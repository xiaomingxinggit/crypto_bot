# exchange/binance/market/future/kline.py
from exchange.binance.api.api import Future
from utils.http_client import http_client
from exchange.binance.model.future import FutureKline
from typing import List, Union, Any

class FutureKlineService:
    """
    币安永续合约K线数据封装（服务类）
    所有方法返回 model 定义的实体类
    """

    def __init__(self):
        self.client = http_client

    def get_klines(self, symbol: str, interval: str, limit: int = 500,
                   start_time: int = None, end_time: int = None) -> Union[List[FutureKline], None]:
        """
        获取K线数据
        :param symbol: 交易对
        :param interval: 时间周期 (1m, 5m, 1h, 1d 等)
        :param limit: 返回条数 (1-1000)
        :param start_time: 开始时间戳 (ms)
        :param end_time: 结束时间戳 (ms)
        :return: FutureKline 对象列表 或 None
        """
        params = {"symbol": symbol, "interval": interval, "limit": limit}
        if start_time:
            params["startTime"] = start_time
        if end_time:
            params["endTime"] = end_time

        data = self.client.get(Future.KLINE, params=params)
        if not data:
            return None

        kline_objects = [FutureKline.from_list(kline_data) for kline_data in data]
        return kline_objects

    def get_continuous_klines(self, pair: str, contract_type: str, interval: str, limit: int = 500,
                              start_time: int = None, end_time: int = None) -> Union[List[FutureKline], None]:
        """
        获取连续合约K线数据
        """
        params = {"pair": pair, "contractType": contract_type, "interval": interval, "limit": limit}
        if start_time:
            params["startTime"] = start_time
        if end_time:
            params["endTime"] = end_time

        data = self.client.get(Future.CONTINUOUS_KLINE, params=params)
        if not data:
            return None

        kline_objects = [FutureKline.from_list(kline_data) for kline_data in data]
        return kline_objects

    def get_index_klines(self, pair: str, interval: str, limit: int = 500,
                         start_time: int = None, end_time: int = None) -> Union[List[FutureKline], None]:
        """
        获取价格指数K线数据
        """
        params = {"pair": pair, "interval": interval, "limit": limit}
        if start_time:
            params["startTime"] = start_time
        if end_time:
            params["endTime"] = end_time

        data = self.client.get(Future.INDEX_KLINE, params=params)
        if not data:
            return None

        kline_objects = [FutureKline.from_list(kline_data) for kline_data in data]
        return kline_objects

    def get_mark_price_klines(self, symbol: str, interval: str, limit: int = 500,
                              start_time: int = None, end_time: int = None) -> Union[List[FutureKline], None]:
        """
        获取标记价格K线数据
        """
        params = {"symbol": symbol, "interval": interval, "limit": limit}
        if start_time:
            params["startTime"] = start_time
        if end_time:
            params["endTime"] = end_time

        data = self.client.get(Future.MARK_PRICE_KLINE, params=params)
        if not data:
            return None

        kline_objects = [FutureKline.from_list(kline_data) for kline_data in data]
        return kline_objects

    def get_premium_index_klines(self, symbol: str, interval: str, limit: int = 500,
                                 start_time: int = None, end_time: int = None) -> Union[List[FutureKline], None]:
        """
        获取溢价指数K线数据
        """
        params = {"symbol": symbol, "interval": interval, "limit": limit}
        if start_time:
            params["startTime"] = start_time
        if end_time:
            params["endTime"] = end_time

        data = self.client.get(Future.PREMIUM_INDEX_KLINE, params=params)
        if not data:
            return None

        kline_objects = [FutureKline.from_list(kline_data) for kline_data in data]
        return kline_objects