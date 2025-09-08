# test/test_market_models_live.py
import sys
import os

# 确保项目根目录在 sys.path 中
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from exchange.binance.market.spot.price import SpotPriceService
from exchange.binance.market.spot.kline import SpotKlineService
from exchange.binance.market.spot.depth import SpotDepthService
from exchange.binance.market.spot.exchange_info import SpotExchangeInfoService

from exchange.binance.market.future.price import FuturePriceService
from exchange.binance.market.future.kline import FutureKlineService
from exchange.binance.market.future.depth import FutureDepthService
from exchange.binance.market.future.exchange_info import FutureExchangeInfoService

from utils.logger import logger


def test_spot_price():
    """测试现货价格接口返回实体类"""
    logger.info("🔍 测试现货价格接口...")
    spot_price = SpotPriceService()

    # 测试单个价格
    price = spot_price.get_price("BTCUSDT")
    if price:
        logger.info(f"✅ SpotPrice 返回成功: {price.symbol} = {price.price}")
    else:
        logger.error("❌ SpotPrice 返回 None")

    # 测试24hr行情
    ticker = spot_price.get_24hr_ticker("BTCUSDT")
    if ticker:
        logger.info(f"✅ Spot24hrTicker 返回成功: {ticker.symbol} | 涨跌幅 {ticker.priceChangePercent}%")
    else:
        logger.error("❌ Spot24hrTicker 返回 None")


def test_spot_kline():
    """测试现货K线接口返回实体类"""
    logger.info("🔍 测试现货K线接口...")
    kline = SpotKlineService()
    data = kline.get_klines("BTCUSDT", "1h", limit=2)
    if data and len(data) > 0:
        latest = data[-1]
        logger.info(f"✅ SpotKline 返回成功: 时间={latest.timestamp}, 开={latest.open}, 收={latest.close}")
    else:
        logger.error("❌ SpotKline 返回 None 或空列表")


def test_spot_depth():
    """测试现货深度接口返回实体类"""
    logger.info("🔍 测试现货订单簿深度...")
    depth = SpotDepthService()
    result = depth.get_depth("BTCUSDT", limit=5)
    if result:
        logger.info(f"✅ SpotDepth 返回成功: bids前5={result.bids[:5]}, asks前5={result.asks[:5]}")
    else:
        logger.error("❌ SpotDepth 返回 None")


def test_spot_exchange_info():
    """测试现货交易对信息"""
    logger.info("🔍 测试现货交易对信息...")
    info = SpotExchangeInfoService()
    result = info.get_exchange_info("BTCUSDT")
    if result:
        symbols = [s['symbol'] for s in result.symbols[:3]]
        logger.info(f"✅ SpotExchangeInfo 返回成功: 支持交易对 {symbols}...")
    else:
        logger.error("❌ SpotExchangeInfo 返回 None")


def test_future_price():
    """测试期货价格接口返回实体类"""
    logger.info("🔍 测试期货价格接口...")
    future_price = FuturePriceService()

    # 测试最新价格
    price = future_price.get_price("BTCUSDT")
    if price:
        logger.info(f"✅ FuturePrice 返回成功: {price.symbol} = {price.price}")
    else:
        logger.error("❌ FuturePrice 返回 None")

    # 测试标记价格
    mark = future_price.get_mark_price("BTCUSDT")
    if mark:
        logger.info(f"✅ FutureMarkPrice 返回成功: 标记价={mark.markPrice}, 资金费率={mark.lastFundingRate}")
    else:
        logger.error("❌ FutureMarkPrice 返回 None")

    # 测试资金费率
    funding = future_price.get_funding_rate_history("BTCUSDT", limit=1)
    if funding and len(funding) > 0:
        logger.info(f"✅ FutureFundingRate 返回成功: 费率={funding[0].fundingRate}")
    else:
        logger.error("❌ FutureFundingRate 返回 None")


def test_future_kline():
    """测试期货K线接口返回实体类"""
    logger.info("🔍 测试期货K线接口...")
    kline = FutureKlineService()
    data = kline.get_klines("BTCUSDT", "1h", limit=2)
    if data and len(data) > 0:
        latest = data[-1]
        logger.info(f"✅ FutureKline 返回成功: 时间={latest.timestamp}, 开={latest.open}, 收={latest.close}")
    else:
        logger.error("❌ FutureKline 返回 None 或空列表")


def test_future_depth():
    """测试期货深度接口返回实体类"""
    logger.info("🔍 测试期货订单簿深度...")
    depth = FutureDepthService()
    result = depth.get_depth("BTCUSDT", limit=5)
    if result:
        logger.info(f"✅ FutureDepth 返回成功: bids前5={result.bids[:5]}, asks前5={result.asks[:5]}")
    else:
        logger.error("❌ FutureDepth 返回 None")


def test_future_exchange_info():
    """测试期货交易对信息"""
    logger.info("🔍 测试期货交易对信息...")
    info = FutureExchangeInfoService()
    result = info.get_exchange_info("BTCUSDT")
    if result:
        symbols = [s['symbol'] for s in result.symbols[:3]]
        logger.info(f"✅ FutureExchangeInfo 返回成功: 支持交易对 {symbols}...")
    else:
        logger.error("❌ FutureExchangeInfo 返回 None")


def main():
    """主测试函数"""
    logger.info("🚀 开始执行期现货模型接口实时测试")

    try:
        test_spot_price()
        test_spot_kline()
        test_spot_depth()
        test_spot_exchange_info()

        test_future_price()
        test_future_kline()
        test_future_depth()
        test_future_exchange_info()

        logger.info("🎉 所有测试完成，全部接口返回实体类成功！")
    except Exception as e:
        logger.error(f"❌ 测试过程中发生异常: {e}")


if __name__ == "__main__":
    main()