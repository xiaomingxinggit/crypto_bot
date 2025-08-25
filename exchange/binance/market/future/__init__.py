# exchange/binance/market/future/__init__.py
from .price import FuturePrice
from .kline import FutureKline
from .depth import FutureDepth
from .trade import FutureTrade
from .exchange_info import FutureExchangeInfo


class FutureMarket:
    """
    币安永续合约市场数据统一入口
    """

    def __init__(self):
        self.price = FuturePrice()
        self.kline = FutureKline()
        self.depth = FutureDepth()
        self.trade = FutureTrade()
        self.exchange_info = FutureExchangeInfo()