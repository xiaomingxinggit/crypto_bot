# test/test_email_notifier.py
import sys
import os

# 确保项目根目录在 sys.path 中
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from notify.email import EmailNotifier
from utils.logger import logger


def test_send_email():
    """测试邮件发送功能"""
    logger.info("📧 开始测试邮件通知功能...")

    try:
        # 初始化邮件通知器
        notifier = EmailNotifier()

        # 发送测试邮件
        subject = "【Crypto Bot】测试邮件"
        content = """
        这是一封来自 Crypto Bot 的测试通知邮件。

        ✅ 项目名称：crypto_bot
        ✅ 当前状态：邮件模块测试通过
        ✅ 发送时间：{}
        """.format(__import__('datetime').datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

        notifier.send(subject, content)

        logger.info("🟢 邮件发送测试成功！请检查收件箱（或垃圾邮件）")
    except Exception as e:
        logger.error(f"🔴 邮件发送失败: {e}")


if __name__ == "__main__":
    test_send_email()