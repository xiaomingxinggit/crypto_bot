# Crypto Bot 项目文档

一个基于 Python 的加密货币机器人项目，专注于非交易功能的实现，支持币安（Binance）现货与永续合约市场的公共数据接口，具备良好的模块化设计和可扩展性。

---

## 📌 项目概述

本项目旨在构建一个轻量级、高可用的加密货币市场数据监控机器人，通过调用币安公开 API 获取现货与期货市场数据，用于行情分析、价格监控、数据采集等非交易场景。

- ✅ 仅使用公开接口，无需 API Key
- ✅ 支持现货（Spot）与永续合约（USDⓈ-M Futures）
- ✅ 模块化设计，易于扩展
- ✅ 内置 HTTP 重试、日志记录、统一异常处理
- ✅ 支持多环境开发（开发 / 测试 / 生产）

---

## 🧩 功能模块

| 模块 | 功能 |
|------|------|
| `exchange/binance/market/spot/` | 现货市场数据封装（价格、K线、深度、成交、交易对信息） |
| `exchange/binance/market/future/` | 永续合约市场数据封装（价格、标记价、资金费率、K线等） |
| `utils/http_client.py` | 统一 HTTP 客户端，支持重试、超时、日志 |
| `utils/logger.py` | 全局日志系统，输出到控制台与 `log/` 文件 |
| `exchange/binance/api/api.py` | 币安现货与期货 API 接口常量定义 |

---

## 🚀 快速开始

### 1. 克隆项目
```bash
git clone <your-repo-url>
cd crypto_bot
```

### 2. 创建虚拟环境
```bash
python -m venv .venv
source .venv/bin/activate  # Linux/Mac
# 或
.venv\Scripts\activate     # Windows
```

### 3. 安装依赖
```bash
pip install requests
```

### 4. 运行测试
```bash
python test/test_binance_market.py
```


## 📊 支持的 API 接口
### 现货（Spot）
- 最新价格 `/api/v3/ticker/price`
- 24小时行情 `/api/v3/ticker/24hr`
- K线数据 `/api/v3/klines`
- 订单簿深度 `/api/v3/depth`
- 交易对信息 `/api/v3/exchangeInfo`
- 标记价格与资金费率 `/api/v3/avgPrice`, `/api/v3/book/ticker`

### 永续合约（USDⓈ-M Futures）
- 最新价格 `/fapi/v1/ticker/price`
- 标记价格 `/fapi/v1/premiumIndex`
- 资金费率 `/fapi/v1/fundingRate`
- K线数据 `/fapi/v1/klines`
- 连续合约K线 `/fapi/v1/continuousKlines`
- 价格指数K线 `/fapi/v1/indexPriceKlines`
- 订单簿深度 `/fapi/v1/depth`

## 📁 项目结构
```
crypto_bot/
├── exchange/
│   └── binance/
│       ├── api/
│       │   └── api.py
│       └── market/
│           ├── future/
│           └── spot/
├── test/
│   └── test_binance_market.py
├── utils/
│   ├── http_client.py
│   └── logger.py
├── log/
├── .gitignore
├── main.py
└── README.md
```

## ⚠️ 注意事项
1. fapi.binance.com 返回 403 错误？
- 浏览器访问 https://fapi.binance.com 会显示 403 ERROR，这是正常现象（CloudFront 阻止直接访问）。
- 不影响程序调用：你的代码通过 requests 仍可正常获取数据。

2. 测试网（Testnet）说明
- 现货测试网地址：https://testnet.binance.vision
- 每月自动重置一次，所有订单和数据清空，但 API Key 保留
- 不支持 /sapi 接口，仅支持 /api 接口
- 资金为虚拟资产，不可提现
> 🔔 提示：从 2025-05-27 起，测试网变更日志（Changelog）不再更新，请通过官方文档获取最新信息。 

3. 时间校验增强（2025-05-21）
- 币安已增加对 recvWindow 的二次校验（在请求进入撮合引擎前）；
- 当前项目仅使用公开接口，不受此变更影响；
- 若未来扩展交易功能，需确保 timestamp 与服务器时间差值在 recvWindow 范围内。


## 📬 未来规划
1. 接入 WebSocket 实时行情
2. 实现通知模块（Telegram、邮件）
3. 支持多交易所（OKX、Bybit）
4. 添加缓存与数据库支持
