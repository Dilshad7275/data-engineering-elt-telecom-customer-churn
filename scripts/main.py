import sys
import os

# Add the 'scripts' directory explicitly to sys.path for all runs
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

# If you want to be sure, add the absolute path to the scripts folder (adjust path if needed)
# sys.path.insert(0, '/opt/airflow/scripts')  # Use absolute path inside container
import argparse
from utils import setup_logger

from extract import find_latest_csv, extract_to_staging
from transform import load_from_staging, transform_dataframe, write_to_production

# rest of your code...


logger = setup_logger()

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

def run_once():
    csv_path = find_latest_csv()
    if not csv_path:
        logger.info("No CSV file found in feed dir. Drop a .csv into data/incoming/")
        return

    try:
        file_name, rows = extract_to_staging(csv_path)
    except Exception as e:
        logger.exception("ETL failed during extract: %s", e)
        return

    try:
        df = load_from_staging()
        df_trans = transform_dataframe(df)
        write_to_production(df_trans)
    except Exception as e:
        logger.exception("ETL failed during transform/load: %s", e)
        return

    logger.info("ETL run completed successfully for file %s (%d rows)", file_name, rows)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--once", action="store_true", help="Run ETL once and exit")
    args = parser.parse_args()
    if args.once:
        run_once()
    else:
        # For now we simply run once. Cron / scheduler will call main.py --once periodically.
        run_once()
