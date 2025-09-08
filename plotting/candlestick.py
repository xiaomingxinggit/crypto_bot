# plotting/candlestick.py
import plotly.graph_objects as go
from datetime import datetime
from typing import List

def plot_klines_plotly(klines: List, symbol: str = "BTCUSDT", interval: str = "1h", save_html: str = None, save_image: str = None):
    """
    使用 Plotly 绘制交互式K线图
    :param klines: SpotKline 或 FutureKline 对象列表
    :param symbol: 交易对
    :param interval: 时间周期
    :param save_html: 保存为HTML文件路径
    :param save_image: 保存为图片路径（支持 .png, .jpg, .svg, .pdf）
    """
    if not klines:
        print("❌ 无K线数据可绘制")
        return

    # 转换数据
    dates = [datetime.fromtimestamp(k.timestamp / 1000) for k in klines]
    opens = [float(k.open) for k in klines]
    highs = [float(k.high) for k in klines]
    lows = [float(k.low) for k in klines]
    closes = [float(k.close) for k in klines]

    # 创建K线图
    fig = go.Figure(data=go.Candlestick(
        x=dates,
        open=opens,
        high=highs,
        low=lows,
        close=closes,
        name="K线"
    ))

    fig.update_layout(
        title=f"{symbol} {interval} K线图",
        xaxis_title="时间",
        yaxis_title="价格 (USDT)",
        xaxis_rangeslider_visible=False,
        hovermode='x unified',
        template='plotly_dark'
    )

    # 保存为 HTML
    if save_html:
        fig.write_html(save_html)
        print(f"✅ 图表已保存为 HTML: {save_html}")

    # 保存为图片
    if save_image:
        # 需要安装 kaleido: pip install kaleido
        fig.write_image(save_image)
        print(f"✅ 图表已保存为图片: {save_image}")

    # 如果都没指定，则显示
    if not save_html and not save_image:
        fig.show()