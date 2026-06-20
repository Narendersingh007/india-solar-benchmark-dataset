from pathlib import Path
from loguru import logger
PROJECT_ROOT = Path(__file__).resolve().parents[2]
LOG_DIR = PROJECT_ROOT / "logs"
LOG_DIR.mkdir(exist_ok=True)
logger.remove()
logger.add(
    LOG_DIR / "pipeline.log",
    rotation="10 MB",
    retention="7 days",
    level="INFO",
)

logger.add(
    sink=lambda msg: print(msg, end=""),
    level="INFO",
)

__all__ = ["logger"]