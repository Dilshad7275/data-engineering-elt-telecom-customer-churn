import logging
import os
from datetime import datetime

def setup_logger(name="etl", logfile=None, level=logging.INFO):
    # logs folder inside the same folder as this script (scripts/logs)
    scripts_dir = os.path.dirname(os.path.abspath(__file__))
    logs_dir = os.path.join(scripts_dir, "logs")
    os.makedirs(logs_dir, exist_ok=True)

    if logfile is None:
        logfile = os.path.join(logs_dir, f"pipeline_{datetime.now().strftime('%Y%m%d')}.log")

    print(f"Logging to file: {logfile}")

    logger = logging.getLogger(name)
    if not logger.handlers:
        logger.setLevel(level)
        fmt = logging.Formatter("%(asctime)s [%(levelname)s] %(message)s")
        fh = logging.FileHandler(logfile)
        fh.setFormatter(fmt)
        ch = logging.StreamHandler()
        ch.setFormatter(fmt)
        logger.addHandler(fh)
        logger.addHandler(ch)
    return logger
