# config.py
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Feed directory where you drop CSV files

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # telecom-etl/
FEED_DIR = os.path.join(BASE_DIR, "data", "incoming")

# Staging & Production table names
STAGING_TABLE = "staging_customers"
PRODUCTION_TABLE = "reporting_customers"

# PII columns to anonymize from staging -> production
PII_COLUMNS = ["CustomerID"]  # adjust if your csv column name differs

# Default fill values for missing data (adjust to your columns)
DEFAULTS = {
    "Age": 30,
    "Gender": "Unknown",
    "Tenure": 0,
    "MonthlyCharges": 0.0,
    "ContractType": "Unknown",
    "InternetService": "Unknown",
    "TotalCharges": 0.0,
    "TechSupp": "Unknown"
}

# Postgres connection details (use the ports you mapped in docker-compose)
PG = {
    "host": os.getenv("PG_HOST", "host.docker.internal"),
    "port": int(os.getenv("PG_PORT", 5432)),
    "user": os.getenv("PG_USER", "postgres"),
    "password": os.getenv("PG_PASSWORD", "postgres"),
    "staging_db": os.getenv("PG_STAGING_DB", "etl_staging_db"),
    "prod_db": os.getenv("PG_PROD_DB", "etl_production_db"),
}

# Build SQLAlchemy URLs
STAGING_DB_URL = f"postgresql+psycopg2://{PG['user']}:{PG['password']}@{PG['host']}:{PG['port']}/{PG['staging_db']}"
PROD_DB_URL = f"postgresql+psycopg2://{PG['user']}:{PG['password']}@{PG['host']}:{PG['port']}/{PG['prod_db']}"
