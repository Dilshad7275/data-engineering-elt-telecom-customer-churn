# load.py
# (optional helpers; here for extensibility — not strictly required)
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from utils import setup_logger
logger = setup_logger()

def record_etl_log(engine_url, file_name, rows_processed, status="success"):
    # If you want to store run metadata in DB, implement here.
    # For simplicity, we leave this a placeholder.
    logger.info("Load: ETL run log - file=%s rows=%d status=%s", file_name, rows_processed, status)
