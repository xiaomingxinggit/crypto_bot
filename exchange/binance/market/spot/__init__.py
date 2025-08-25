# exchange/binance/market/spot/__init__.py
from .price import SpotPrice
from .kline import SpotKline
from .depth import SpotDepth
from .trade import SpotTrade
from .exchange_info import SpotExchangeInfo


class SpotMarket:
    """
    币安现货市场数据统一入口
    """

    def __init__(self):
        self.price = SpotPrice()
        self.kline = SpotKline()
        self.depth = SpotDepth()
        self.trade = SpotTrade()
        self.exchange_info = SpotExchangeInfo()