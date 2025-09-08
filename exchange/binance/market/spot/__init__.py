# exchange/binance/market/spot/__init__.py
from .price import SpotPriceService
from .kline import SpotKlineService
from .depth import SpotDepthService
from .trade import SpotTradeService
from .exchange_info import SpotExchangeInfoService


class SpotMarket:
    """
    币安现货市场数据统一入口
    """

    def __init__(self):
        self.price = SpotPriceService()
        self.kline = SpotKlineService()
        self.depth = SpotDepthService()
        self.trade = SpotTradeService()
        self.exchange_info = SpotExchangeInfoService()