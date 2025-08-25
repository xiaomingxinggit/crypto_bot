# notify/email.py
import smtplib
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv
from utils.logger import logger

# 加载本地配置
load_dotenv(dotenv_path=os.path.join(os.path.dirname(os.path.dirname(__file__)), ".env.local"))

class EmailNotifier:
    """
    QQ邮箱通知模块（基于SMTP）
    用于发送机器人运行状态、异常告警等通知
    """

    def __init__(self):
        self.host = os.getenv("EMAIL_HOST")
        self.port = int(os.getenv("EMAIL_PORT", 587))
        self.user = os.getenv("EMAIL_USER")
        self.password = os.getenv("EMAIL_PASSWORD")
        self.use_tls = os.getenv("EMAIL_USE_TLS", "True").lower() == "true"
        self.receiver = os.getenv("EMAIL_RECEIVE") or self.user

        if not all([self.host, self.port, self.user, self.password]):
            logger.error("❌ 邮件配置不完整，请检查 .env.local 文件")
            raise ValueError("邮件配置缺失")

        logger.info(f"✅ 邮件通知模块已初始化: {self.user} -> {self.receiver}")

    def send(self, subject: str, content: str, content_type: str = "plain"):
        """
        发送邮件
        :param subject: 邮件标题
        :param content: 邮件内容
        :param content_type: 内容类型: plain / html
        """
        try:
            # 创建MIME对象
            msg = MIMEMultipart()
            msg["From"] = self.user
            msg["To"] = self.receiver
            msg["Subject"] = subject

            # 添加正文
            body = MIMEText(content, content_type, "utf-8")
            msg.attach(body)

            # 连接服务器并发送
            server = smtplib.SMTP(self.host, self.port)
            if self.use_tls:
                server.starttls()
            server.login(self.user, self.password)
            server.sendmail(self.user, self.receiver, msg.as_string())
            server.quit()

            logger.info(f"📨 邮件发送成功 | 标题: {subject}")

        except Exception as e:
            logger.error(f"❌ 邮件发送失败 | 错误: {e}")
            raise