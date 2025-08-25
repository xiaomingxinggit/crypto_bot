# exchange/binance/market/spot/depth.py
from exchange.binance.api.api import Spot
from utils.http_client import http_client
from typing import Union, Dict, Any

class SpotDepth:
    """
    币安现货订单簿深度接口封装
    """

    def __init__(self):
        self.client = http_client

    def get_depth(self, symbol: str, limit: int = 100) -> Union[Dict[str, Any], None]:
        """
        获取订单簿深度
        :param symbol: 交易对
        :param limit: 深度条数 (5, 10, 20, 50, 100, 500, 1000, 5000)
        """
        params = {"symbol": symbol, "limit": limit}
        return self.client.get(Spot.DEPTH, params=params)