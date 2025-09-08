# exchange/binance/market/spot/price.py
from exchange.binance.api.api import Spot
from utils.http_client import http_client
from exchange.binance.model.spot import SpotPrice, SpotKline, Spot24hrTicker
from typing import Union, List, Dict, Any

class SpotPriceService:
    """
    币安现货价格接口封装
    所有方法返回 model 定义的实体类
    """

    def __init__(self):
        self.client = http_client

    def get_price(self, symbol: str = None) -> Union[SpotPrice, List[SpotPrice], None]:
        """获取最新价格"""
        params = {"symbol": symbol} if symbol else {}
        data = self.client.get(Spot.TICKER_PRICE, params=params)
        if not data:
            return None
        if isinstance(data, list):
            return [SpotPrice(symbol=item['symbol'], price=item['price']) for item in data]
        return SpotPrice(symbol=data['symbol'], price=data['price'])

    def get_24hr_ticker(self, symbol: str = None) -> Union[Spot24hrTicker, List[Spot24hrTicker], None]:
        """获取24小时行情"""
        params = {"symbol": symbol} if symbol else {}
        data = self.client.get(Spot.TICKER_24HR, params=params)
        if not data:
            return None
        if isinstance(data, list):
            return [Spot24hrTicker(**item) for item in data]
        return Spot24hrTicker(**data)

    # def get_avg_price(self, symbol: str) -> Union[Dict[str, Any], None]:
    #     """获取加权平均价（当前返回原始数据，暂无专用模型）"""
    #     if not symbol:
    #         raise ValueError("symbol is required")
    #     return self.client.get(Spot.AVG_PRICE, params={"symbol": symbol})
    #
    # def get_best_ticker(self, symbol: str = None) -> Union[Dict[str, Any], list, None]:
    #     """获取最优挂单（暂未使用 model，因结构简单）"""
    #     params = {"symbol": symbol} if symbol else {}
    #     return self.client.get(Spot.BEST_TICK, params=params)
    #
    # def get_all_book_tickers(self) -> Union[list, None]:
    #     """获取所有最优挂单（暂未使用 model，因结构简单）"""
    #     return self.client.get(Spot.ALL_BOOK_TICKS)