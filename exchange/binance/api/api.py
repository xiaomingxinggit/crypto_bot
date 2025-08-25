# exchange/binance/api/api.py
"""
币安（Binance）所有公开 API 接口 URL 常量定义
✅ 与官方接口逻辑保持一致
✅ 支持现货、合约（USDⓈ-M）等产品线
✅ 可扩展性强，便于后续封装请求
"""


class Spot:
    """现货（Spot/Margin）API"""
    BASE_URL = "https://api.binance.com"

    # 市场数据
    TICKER_PRICE = f"{BASE_URL}/api/v3/ticker/price"           # 最新价格
    TICKER_24HR = f"{BASE_URL}/api/v3/ticker/24hr"             # 24小时行情
    KLINE = f"{BASE_URL}/api/v3/klines"                        # K线数据
    UIKLINES = f"{BASE_URL}/api/v3/uiKlines"                   # 前端优化K线数据
    DEPTH = f"{BASE_URL}/api/v3/depth"                         # 订单簿深度
    EXCHANGE_INFO = f"{BASE_URL}/api/v3/exchangeInfo"          # 交易对信息
    RECENT_TRADES = f"{BASE_URL}/api/v3/trades"                # 最近成交
    AGGREGATE_TRADES = f"{BASE_URL}/api/v3/aggTrades"          # 聚合成交
    AVG_PRICE = f"{BASE_URL}/api/v3/avgPrice"                  # 当前平均价格
    BEST_TICK = f"{BASE_URL}/api/v3/book/ticker"               # 最优挂单（单个交易对）
    ALL_BOOK_TICKS = f"{BASE_URL}/api/v3/ticker/bookTicker"   # 所有最优挂单

    # WebSocket 流（公共）
    WEBSOCKET_STREAM = "wss://stream.binance.com:9443/ws"


class Future:
    """永续合约（USDⓈ-M Futures）API"""
    BASE_URL = "https://fapi.binance.com"

    # 市场数据
    PING = f"{BASE_URL}/fapi/v1/ping"                        # 测试服务器连通性
    SERVER_TIME = f"{BASE_URL}/fapi/v1/time"                 # 获取服务器时间
    EXCHANGE_INFO = f"{BASE_URL}/fapi/v1/exchangeInfo"       # 获取交易规则和交易对
    FUTURE_EXCHANGE_INFO = f"{BASE_URL}/fapi/v1/exchangeInfo"  # 合约下架日期
    DEPTH = f"{BASE_URL}/fapi/v1/depth"                      # 深度信息
    RECENT_TRADES = f"{BASE_URL}/fapi/v1/trades"             # 近期成交
    AGGREGATE_TRADES = f"{BASE_URL}/fapi/v1/aggTrades"       # 查询历史成交(MARKET-DATA)
    KLINE = f"{BASE_URL}/fapi/v1/klines"                     # K线数据
    CONTINUOUS_KLINE = f"{BASE_URL}/fapi/v1/continuousKlines"  # 连续合约K线数据
    INDEX_KLINE = f"{BASE_URL}/fapi/v1/indexPriceKlines"     # 价格指数K线数据
    MARK_PRICE_KLINE = f"{BASE_URL}/fapi/v1/markPriceKlines" # 标记价格K线数据
    PREMIUM_INDEX_KLINE = f"{BASE_URL}/fapi/v1/premiumIndexKlines"  # 溢价指数K线数据
    LATEST_MARK_PRICE = f"{BASE_URL}/fapi/v1/premiumIndex"   # 最新标记价格和资金费率
    FUNDING_RATE_HISTORY = f"{BASE_URL}/fapi/v1/fundingRate" # 查询资金费率历史
    FUNDING_RATE_INFO = f"{BASE_URL}/fapi/v1/fundingRate"    # 查询资金费率信息
    TICKER_24HR = f"{BASE_URL}/fapi/v1/ticker/24hr"          # 24hr价格变动情况
    TICKER_PRICE_V2 = f"{BASE_URL}/fapi/v1/ticker/price"     # 最新价格V2
    BEST_TICK = f"{BASE_URL}/fapi/v1/book/ticker"            # 当前最优挂单
    QUARTERLY_SETTLEMENT = f"{BASE_URL}/fapi/v1/quarterlySettlement"  # 季度合约历史结算价
    OPEN_INTEREST = f"{BASE_URL}/fapi/v1/openInterest"       # 获取未平仓合约数
    OPEN_INTEREST_HISTORY = f"{BASE_URL}/fapi/v1/openInterestHist"  # 合约持仓量历史
    LONG_SHORT_RATIO = f"{BASE_URL}/fapi/v1/longShortRatio"  # 大户持仓量多空比
    ACCOUNT_RATIO = f"{BASE_URL}/fapi/v1/accountRatio"       # 大户账户数多空比
    LONG_SHORT_COUNT = f"{BASE_URL}/fapi/v1/longShortCount"  # 多空持仓人数比
    ACTIVE_BUY_SELL = f"{BASE_URL}/fapi/v1/activeBuySell"    # 合约主动买卖量
    BASIS = f"{BASE_URL}/fapi/v1/basis"                      # 基差
    COMPOSITE_INDEX = f"{BASE_URL}/fapi/v1/compositeIndex"   # 综合指数交易对信息
    ASSET_INDEX = f"{BASE_URL}/fapi/v1/assetIndex"           # 多资产模式资产汇率指数
    INDEX_COMPONENTS = f"{BASE_URL}/fapi/v1/indexComponents" # 查询指数价格成分
    INSURANCE_FUND = f"{BASE_URL}/fapi/v1/insuranceFund"    # 查询保险基金余额快照

    # WebSocket 流（公共）
    WEBSOCKET_STREAM = "wss://fstream.binance.com/ws"


# ====================
# 可选：测试网地址（用于调试）
# ====================

class SpotTestnet:
    """现货测试网"""
    BASE_URL = "https://testnet.binance.vision"

    TICKER_PRICE = f"{BASE_URL}/api/v3/ticker/price"
    KLINE = f"{BASE_URL}/api/v3/klines"
    EXCHANGE_INFO = f"{BASE_URL}/api/v3/exchangeInfo"
    WEBSOCKET_STREAM = "wss://testnet.binance.vision/ws"


class FutureTestnet:
    """合约测试网"""
    BASE_URL = "https://testnet.binancefuture.com"

    TICKER_PRICE = f"{BASE_URL}/fapi/v1/ticker/price"
    KLINE = f"{BASE_URL}/fapi/v1/klines"
    EXCHANGE_INFO = f"{BASE_URL}/fapi/v1/exchangeInfo"
    WEBSOCKET_STREAM = "wss://testnet.binancefuture.com/ws"


