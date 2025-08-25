# utils/logger.py
import logging
import os
from datetime import datetime

# ==================== 配置区 ====================
LOG_DIR = "log"
os.makedirs(LOG_DIR, exist_ok=True)

# 当前日期日志文件
def get_log_file():
    return os.path.join(LOG_DIR, f"{datetime.now().strftime('%Y-%m-%d')}.log")

# ==================== 全局 Logger ====================
logger = logging.getLogger("crypto_bot")
logger.setLevel(logging.DEBUG)

# 防止重复添加处理器（重要！）
if not logger.handlers:
    # 格式化器：简洁清晰，包含时间、级别、消息
    formatter = logging.Formatter(
        fmt="[%(asctime)s] %(levelname)s | %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )

    # 控制台处理器
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)
    console_handler.setFormatter(formatter)

    # 文件处理器（自动按天切换，无需轮转库）
    file_handler = logging.FileHandler(get_log_file(), encoding="utf-8")
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(formatter)

    # 添加处理器
    logger.addHandler(console_handler)
    logger.addHandler(file_handler)
