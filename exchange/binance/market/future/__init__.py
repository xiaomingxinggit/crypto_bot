# exchange/binance/market/future/__init__.py
from .price import FuturePriceService
from .kline import FutureKlineService
from .depth import FutureDepthService
from .trade import FutureTradeService
from .exchange_info import FutureExchangeInfoService


class FutureMarket:
    """
    币安永续合约市场数据统一入口
    """

    def __init__(self):
        self.price = FuturePriceService()
        self.kline = FutureKlineService()
        self.depth = FutureDepthService()
        self.trade = FutureTradeService()
        self.exchange_info = FutureExchangeInfoService()