# exchange/binance/market/future/trade.py
from exchange.binance.api.api import Future
from utils.http_client import http_client
from typing import Union, List, Any

class FutureTrade:
    """
    币安永续合约成交记录接口封装
    """

    def __init__(self):
        self.client = http_client

    def get_recent_trades(self, symbol: str, limit: int = 500) -> Union[List[Any], None]:
        """获取近期成交记录"""
        params = {"symbol": symbol, "limit": limit}
        return self.client.get(Future.RECENT_TRADES, params=params)

    def get_aggregate_trades(self, symbol: str, limit: int = 500,
                           from_id: int = None, start_time: int = None, end_time: int = None) -> Union[List[Any], None]:
        """获取聚合成交记录"""
        params = {"symbol": symbol, "limit": limit}
        if from_id:
            params["fromId"] = from_id
        if start_time:
            params["startTime"] = start_time
        if end_time:
            params["endTime"] = end_time
        return self.client.get(Future.AGGREGATE_TRADES, params=params)