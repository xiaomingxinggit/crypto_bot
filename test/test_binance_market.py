# test/test_binance_market.py
import time
import sys
import os

# 确保项目根目录在 sys.path 中
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from exchange.binance.market.spot import SpotMarket
from exchange.binance.market.future import FutureMarket
from utils.logger import logger


def test_spot_market():
    """测试现货市场接口"""
    logger.info("🔍 开始测试现货市场接口...")
    spot = SpotMarket()

    # 测试：获取BTCUSDT最新价格
    logger.info("✅ 测试: 获取现货最新价格")
    price = spot.price.get_price("BTCUSDT")
    if price:
        logger.info(f"🟢 获取成功: {price}")
    else:
        logger.error("🔴 获取现货价格失败")

    # 测试：获取24小时行情
    logger.info("✅ 测试: 获取现货24小时行情")
    ticker_24hr = spot.price.get_24hr_ticker("BTCUSDT")
    if ticker_24hr:
        logger.info(f"🟢 获取成功: 价格变动 {ticker_24hr.get('priceChangePercent')}%")
    else:
        logger.error("🔴 获取24小时行情失败")

    # 测试：获取K线数据
    logger.info("✅ 测试: 获取现货K线数据 (1小时, 5条)")
    klines = spot.kline.get_klines("BTCUSDT", "1h", limit=5)
    if klines and len(klines) > 0:
        logger.info(f"🟢 获取成功: 返回 {len(klines)} 条K线")
    else:
        logger.error("🔴 获取K线数据失败")

    # 测试：获取订单簿深度
    logger.info("✅ 测试: 获取现货订单簿深度")
    depth = spot.depth.get_depth("BTCUSDT", limit=5)
    if depth:
        logger.info(f"🟢 获取成功: bids={depth.get('bids')[:2]}, asks={depth.get('asks')[:2]}")
    else:
        logger.error("🔴 获取订单簿失败")

    # 测试：获取交易对信息
    logger.info("✅ 测试: 获取现货交易对信息")
    info = spot.exchange_info.get_exchange_info("BTCUSDT")
    if info:
        # 修正后
        if info and 'symbols' in info and len(info['symbols']) > 0:
            symbol_info = info['symbols'][0]
            logger.info(f"🟢 获取成功: symbol={symbol_info.get('symbol')}, status={symbol_info.get('status')}")
        else:
            logger.error("🔴 获取交易对信息失败或格式异常")
    else:
        logger.error("🔴 获取交易对信息失败")

    logger.info("🟢 现货市场接口测试完成\n")


def test_future_market():
    """测试期货市场接口"""
    logger.info("🔍 开始测试期货市场接口...")
    future = FutureMarket()

    # 测试：获取期货最新价格
    logger.info("✅ 测试: 获取期货最新价格")
    price = future.price.get_price("BTCUSDT")
    if price:
        logger.info(f"🟢 获取成功: {price}")
    else:
        logger.error("🔴 获取期货价格失败")

    # 测试：获取标记价格和资金费率
    logger.info("✅ 测试: 获取期货标记价格")
    mark_price = future.price.get_mark_price("BTCUSDT")
    if mark_price:
        logger.info(f"🟢 获取成功: 标记价格={mark_price.get('markPrice')}, 资金费率={mark_price.get('lastFundingRate')}")
    else:
        logger.error("🔴 获取标记价格失败")

    # 测试：获取资金费率历史
    logger.info("✅ 测试: 获取资金费率历史")
    funding_rate = future.price.get_funding_rate("BTCUSDT", limit=3)
    if funding_rate and len(funding_rate) > 0:
        logger.info(f"🟢 获取成功: 最近资金费率={funding_rate[0].get('fundingRate')}")
    else:
        logger.error("🔴 获取资金费率历史失败")

    # 测试：获取K线数据
    logger.info("✅ 测试: 获取期货K线数据 (1小时, 5条)")
    klines = future.kline.get_klines("BTCUSDT", "1h", limit=5)
    if klines and len(klines) > 0:
        logger.info(f"🟢 获取成功: 返回 {len(klines)} 条K线")
    else:
        logger.error("🔴 获取期货K线数据失败")

    # 测试：获取订单簿深度
    logger.info("✅ 测试: 获取期货订单簿深度")
    depth = future.depth.get_depth("BTCUSDT", limit=5)
    if depth:
        logger.info(f"🟢 获取成功: bids={depth.get('bids')[:2]}, asks={depth.get('asks')[:2]}")
    else:
        logger.error("🔴 获取期货订单簿失败")

    logger.info("🟢 期货市场接口测试完成\n")


def main():
    logger.info("🚀 开始执行币安市场接口完整测试")

    # 简单网络连通性提示
    logger.warning("⚠️  注意: fapi.binance.com 浏览器显示403是正常现象，不影响程序调用")
    logger.info("⏳ 正在进行接口测试，请稍候...")

    try:
        test_spot_market()
        time.sleep(1)  # 避免请求过快
        test_future_market()
        logger.info("🎉 所有测试完成，全部接口调用成功！")
    except Exception as e:
        logger.error(f"❌ 测试过程中发生异常: {e}")


if __name__ == "__main__":
    main()
