# exchange/binance/market/spot/depth.py
from exchange.binance.api.api import Spot
from utils.http_client import http_client
from exchange.binance.model.spot import SpotDepth
from typing import Union, Dict, Any

class SpotDepthService:
    """
    币安现货订单簿深度接口封装（服务类）
    返回 model 定义的 SpotDepth 实体类
    """

    def __init__(self):
        self.client = http_client

    def get_depth(self, symbol: str, limit: int = 100) -> Union[SpotDepth, None]:
        """
        获取订单簿深度
        :param symbol: 交易对
        :param limit: 深度条数 (5, 10, 20, 50, 100, 500, 1000, 5000)
        :return: SpotDepth 对象 或 None
        """
        params = {"symbol": symbol, "limit": limit}
        data = self.client.get(Spot.DEPTH, params=params)
        if not data:
            return None

        try:
            bids = [[price, qty] for price, qty in data["bids"]]
            asks = [[price, qty] for price, qty in data["asks"]]
            return SpotDepth(bids=bids, asks=asks)
        except KeyError as e:
            print(f"❌ 数据字段缺失: {e}")
            return None