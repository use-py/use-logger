from datetime import timezone, timedelta

from loguru import logger

from usepy_plugin_logger import useLogger

tz = timezone(timedelta(hours=-9))
useLogger(tz=tz)

logger.debug("Hello, world!")

