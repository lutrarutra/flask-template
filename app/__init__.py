import sys, os
from loguru import logger

logger.remove()

__fmt = """<level>{level}</level> @ {time:YYYY-MM-DD HH:mm:ss} ({file}:{line} in {function}):
>   <white>{message}</white>"""

if os.getenv("FLASK_DEBUG") == "1":
    logger.add(
        sys.stdout, colorize=True,
        format=__fmt, level="DEBUG"
    )
else:
    logger.add(
        sys.stdout, colorize=True,
        format=__fmt, level="INFO"
    )