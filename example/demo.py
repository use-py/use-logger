import logging

from use_logger.formatters import JsonFormatter
from use_logger.handlers import LogstashHandler


def useLogger():
    # 创建日志格式
    formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )

    # 创建处理器（handler）
    handler = LogstashHandler(JsonFormatter())
    handler.setFormatter(JsonFormatter())

    # 获取根日志记录器并设置处理器
    root_logger = logging.getLogger()
    root_logger.addHandler(handler)
    root_logger.setLevel(logging.DEBUG)


if __name__ == "__main__":
    useLogger()

    logger = logging.getLogger(__name__)

    logger.debug("xxxx")
