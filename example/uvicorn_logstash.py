from use_logger import useLogger
from use_logger.handlers import logstash_handler
from loguru import logger
from usepy.plugin import useLogger as useLogger1

useLogger1("test")

useLogger(
    handlers=[
        logstash_handler(level="DEBUG", extra={"app_name": "spider"})
    ],
    packages=["usepy"],  # hook拦截 usepy 的日志
    extra={"project_name": "usepy"}
)

logger.warning("test warning")
logger.info("test info")
logger.debug("test debug")
# 这里测试调用函数的耗时，这是一个在usepy包中的函数



