from datetime import timedelta, timezone

from loguru import logger

from use_logger import useLogger, useLoggerHandlers

tz = timezone(timedelta(hours=-9))
useLogger(handlers=[useLoggerHandlers.logstash_handler()], tz=tz)

logger.info("Hello, world!")
