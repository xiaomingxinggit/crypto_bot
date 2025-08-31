# exchange/binance/model/spot.py
from dataclasses import dataclass, field
from typing import List, Optional, Dict, Any
import json


@dataclass
class SpotPrice:
    """现货最新价格"""
    symbol: str
    price: str


@dataclass
class Spot24hrTicker:
    """24小时行情数据"""
    symbol: str
    priceChange: str
    priceChangePercent: str
    weightedAvgPrice: str
    prevClosePrice: str
    lastPrice: str
    lastQty: str
    bidPrice: str
    bidQty: str
    askPrice: str
    askQty: str
    openPrice: str
    highPrice: str
    lowPrice: str
    volume: str
    quoteVolume: str
    openTime: int
    closeTime: int
    firstId: int
    lastId: int
    count: int


@dataclass
class SpotKline:
    """K线数据"""
    timestamp: int
    open: float
    high: float
    low: float
    close: float
    volume: float
    close_time: int
    quote_asset_volume: float
    number_of_trades: int
    taker_buy_base_asset_volume: float
    taker_buy_quote_asset_volume: float
    ignore: float

    @classmethod
    def from_list(cls, kline_data: List[Any]):
        """从API返回的列表创建对象"""
        return cls(
            timestamp=int(kline_data[0]),
            open=float(kline_data[1]),
            high=float(kline_data[2]),
            low=float(kline_data[3]),
            close=float(kline_data[4]),
            volume=float(kline_data[5]),
            close_time=int(kline_data[6]),
            quote_asset_volume=float(kline_data[7]),
            number_of_trades=int(kline_data[8]),
            taker_buy_base_asset_volume=float(kline_data[9]),
            taker_buy_quote_asset_volume=float(kline_data[10]),
            ignore=float(kline_data[11])
        )


@dataclass
class SpotDepth:
    """订单簿深度"""
    bids: List[List[str]]
    asks: List[List[str]]


@dataclass
class SpotExchangeInfo:
    """交易对信息"""
    timezone: str
    serverTime: int
    rateLimits: List[Dict[str, Any]]
    symbols: List[Dict[str, Any]]
    exchangeFilters: List[Dict[str, Any]]