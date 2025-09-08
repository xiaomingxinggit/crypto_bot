# exchange/binance/model/future.py
from dataclasses import dataclass, field
from typing import List, Optional, Dict, Any
import json


@dataclass
class FuturePrice:
    """期货最新价格"""
    symbol: str
    price: str
    time: int


@dataclass
class FutureMarkPrice:
    """标记价格与资金费率"""
    symbol: str
    markPrice: str
    indexPrice: str
    estimatedSettlePrice: str
    lastFundingRate: str
    nextFundingTime: int
    interestRate: str
    time: int


@dataclass
class FutureFundingRate:
    """资金费率记录"""
    symbol: str
    fundingRate: str
    fundingTime: int
    markPrice: str
    # time: int


@dataclass
class FutureKline:
    """期货K线数据"""
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
class FutureDepth:
    """期货订单簿深度"""
    bids: List[List[str]]
    asks: List[List[str]]


@dataclass
class FutureExchangeInfo:
    """期货交易对信息"""
    timezone: str
    serverTime: int
    rateLimits: List[Dict[str, Any]]
    exchangeFilters: List[Dict[str, Any]]
    symbols: List[Dict[str, Any]]