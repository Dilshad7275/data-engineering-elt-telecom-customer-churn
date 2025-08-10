import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import pandas as pd
from pathlib import Path
from sqlalchemy import create_engine
from config import FEED_DIR, STAGING_TABLE, STAGING_DB_URL
from utils import setup_logger

logger = setup_logger()

def find_latest_csv(feed_dir=FEED_DIR):
    p = Path(feed_dir)
    if not p.exists():
        logger.warning("Feed dir does not exist: %s", feed_dir)
        return None
    csvs = sorted([x for x in p.glob("*.csv") if x.is_file()])
    if not csvs:
        return None
    return csvs[-1]

def extract_to_staging(csv_path, engine_url=STAGING_DB_URL, table_name=STAGING_TABLE):
    logger.info("Extract: reading CSV %s", csv_path)
    df = pd.read_csv(csv_path)
    logger.info("Extract: got dataframe shape %s", df.shape)
    try:
        engine = create_engine(engine_url)
        with engine.connect() as conn:
            # Pass SQLAlchemy connection, not raw DBAPI connection
            df.to_sql(table_name, conn, if_exists="append", index=False, method="multi", chunksize=1000)
        logger.info("Extract: wrote %d rows to staging table %s", len(df), table_name)
    except Exception as e:
        logger.exception("Extract: failed to write to staging: %s", e)
        raise
    return csv_path.name, len(df)
