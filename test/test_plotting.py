# test/test_plotting.py
from exchange.binance.market.spot.kline import SpotKlineService
from plotting import plot_klines_plotly

spot_kline = SpotKlineService()
klines = spot_kline.get_klines("BTCUSDT", "1h", limit=50)

# 保存为 PNG 图片
plot_klines_plotly(klines, symbol="BTCUSDT", interval="1h", save_image="price_trend.png")

# # 同时保存为 HTML 和 图片
# plot_price_trend_interactive(
#     klines,
#     symbol="BTCUSDT",
#     interval="1h",
#     save_html="trend.html",
#     save_image="trend.png"
# )