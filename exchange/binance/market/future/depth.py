# exchange/binance/market/future/depth.py
from exchange.binance.api.api import Future
from utils.http_client import http_client
from typing import Union, Dict, Any

class FutureDepth:
    """
    币安永续合约订单簿深度接口封装
    """

    def __init__(self):
        self.client = http_client

    def get_depth(self, symbol: str, limit: int = 100) -> Union[Dict[str, Any], None]:
        """获取订单簿深度"""
        params = {"symbol": symbol, "limit": limit}
        return self.client.get(Future.DEPTH, params=params)