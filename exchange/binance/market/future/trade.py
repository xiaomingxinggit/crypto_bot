# exchange/binance/market/future/trade.py
from exchange.binance.api.api import Future
from utils.http_client import http_client
from typing import List, Union, Any, Dict

class FutureTradeService:
    """
    币安永续合约成交记录接口封装（服务类）
    暂不使用独立模型类（因结构简单，返回原始字典列表）
    """

    def __init__(self):
        self.client = http_client

    def get_recent_trades(self, symbol: str, limit: int = 500) -> Union[List[Dict[str, Any]], None]:
        """
        获取近期成交记录
        :param symbol: 交易对
        :param limit: 返回条数 (1-1000)
        :return: 成交记录列表 或 None
        """
        params = {"symbol": symbol, "limit": limit}
        return self.client.get(Future.RECENT_TRADES, params=params)

    def get_aggregate_trades(self, symbol: str, limit: int = 500,
                           from_id: int = None, start_time: int = None, end_time: int = None) -> Union[List[Dict[str, Any]], None]:
        """
        获取聚合成交记录
        :param symbol: 交易对
        :param limit: 返回条数
        :param from_id: 从哪条成交 ID 开始
        :param start_time: 开始时间戳 (ms)
        :param end_time: 结束时间戳 (ms)
        :return: 聚合成交列表 或 None
        """
        params = {"symbol": symbol, "limit": limit}
        if from_id:
            params["fromId"] = from_id
        if start_time:
            params["startTime"] = start_time
        if end_time:
            params["endTime"] = end_time
        return self.client.get(Future.AGGREGATE_TRADES, params=params)