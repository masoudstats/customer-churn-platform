from loguru import logger

logger.add(
    "logs/project.log",
    rotation="10 MB",
    retention="10 days",
    level="INFO"
)