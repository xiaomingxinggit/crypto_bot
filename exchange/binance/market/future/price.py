# exchange/binance/market/future/price.py
from exchange.binance.api.api import Future
from utils.http_client import http_client
from exchange.binance.model.future import FuturePrice, FutureMarkPrice, FutureFundingRate
from typing import Union, List, Any

class FuturePriceService:
    """
    币安永续合约价格数据封装（服务类）
    所有方法返回 model 定义的实体类
    """

    def __init__(self):
        self.client = http_client

    def get_price(self, symbol: str = None) -> Union[FuturePrice, List[FuturePrice], None]:
        """
        获取合约最新价格
        """
        params = {"symbol": symbol} if symbol else {}
        data = self.client.get(Future.TICKER_PRICE_V2, params=params)
        if not data:
            return None
        if isinstance(data, list):
            return [FuturePrice(symbol=item['symbol'], price=item['price'], time=item['time']) for item in data]
        return FuturePrice(symbol=data['symbol'], price=data['price'], time=data['time'])

    def get_mark_price(self, symbol: str = None) -> Union[FutureMarkPrice, List[FutureMarkPrice], None]:
        """
        获取标记价格和资金费率
        """
        params = {"symbol": symbol} if symbol else {}
        data = self.client.get(Future.LATEST_MARK_PRICE, params=params)
        if not data:
            return None
        if isinstance(data, list):
            return [FutureMarkPrice(**item) for item in data]
        return FutureMarkPrice(**data)

    def get_funding_rate_history(self, symbol: str, limit: int = 100) -> Union[List[FutureFundingRate], None]:
        """
        查询资金费率历史
        """
        params = {"symbol": symbol, "limit": limit}
        data = self.client.get(Future.FUNDING_RATE_HISTORY, params=params)
        if not data:
            return None
        return [FutureFundingRate(**item) for item in data]

    def get_best_ticker(self, symbol: str = None) -> Union[dict, list, None]:
        """
        获取最优挂单价格（暂不转换为模型，结构简单）
        """
        params = {"symbol": symbol} if symbol else {}
        return self.client.get(Future.BEST_TICK, params=params)

    def get_24hr_ticker(self, symbol: str = None) -> Union[dict, list, None]:
        """
        获取24小时行情（暂不转换为模型，后续可扩展）
        """
        params = {"symbol": symbol} if symbol else {}
        return self.client.get(Future.TICKER_24HR, params=params)