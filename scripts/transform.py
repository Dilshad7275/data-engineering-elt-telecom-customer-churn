# transform.py
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import hashlib
import pandas as pd
from sqlalchemy import create_engine
from config import STAGING_DB_URL, PROD_DB_URL, STAGING_TABLE, PRODUCTION_TABLE, PII_COLUMNS, DEFAULTS
from utils import setup_logger

logger = setup_logger()

def anonymize_value(v):
    if pd.isna(v) or v == "":
        return None
    return hashlib.sha256(str(v).encode("utf-8")).hexdigest()[:16]

def load_from_staging(engine_url=STAGING_DB_URL, table=STAGING_TABLE):
    try:
        engine = create_engine(engine_url)
        df = pd.read_sql_table(table, engine)
        logger.info("Transform: loaded %d rows from staging", len(df))
        return df
    except Exception as e:
        logger.exception("Transform: error reading staging table: %s", e)
        raise

def transform_dataframe(df: pd.DataFrame) -> pd.DataFrame:
    logger.info("Transform: starting cleaning & anonymization")
    # Fill defaults for missing columns present in df
    for col, val in DEFAULTS.items():
        if col in df.columns:
            df[col] = df[col].fillna(val)

    # For object/string columns not in DEFAULTS, fill with 'UNKNOWN'
    for col in df.select_dtypes(include=["object"]).columns:
        if col not in DEFAULTS:
            df[col] = df[col].fillna("UNKNOWN")

    # Anonymize PII columns if present
    for col in PII_COLUMNS:
        if col in df.columns:
            df[col] = df[col].apply(anonymize_value)

    # Example derived column (optional) - keep simple: flag for high monthly charges
    if "MonthlyCharges" in df.columns:
        df["HighChargesFlag"] = df["MonthlyCharges"].apply(lambda x: 1 if x and float(x) > 80 else 0)

    logger.info("Transform: transformation complete")
    return df

def write_to_production(df: pd.DataFrame, engine_url=PROD_DB_URL, table=PRODUCTION_TABLE):
    try:
        engine = create_engine(engine_url)
        # replace reporting table each run (simple, idempotent for demo)
        df.to_sql(table, engine, if_exists="replace", index=False, method="multi", chunksize=1000)
        logger.info("Transform: wrote %d rows to production table %s", len(df), table)
    except Exception as e:
        logger.exception("Transform: failed to write production: %s", e)
        raise
