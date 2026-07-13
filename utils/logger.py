import logging
from pathlib import Path

# Create logs directory if it doesn't exist
LOG_DIR = Path("logs")
LOG_DIR.mkdir(parents=True, exist_ok=True)

# Log file
LOG_FILE = LOG_DIR / "app.log"

logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
)

logger = logging.getLogger("MeetingNotesAgent")


def log_info(message: str):
    logger.info(message)


def log_error(message: str):
    logger.error(message)