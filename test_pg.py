from sqlalchemy import create_engine
import pandas as pd

engine = create_engine("postgresql+psycopg2://postgres:postgres@localhost:5432/etl_staging_db")

df = pd.DataFrame({
    "id": [1, 2, 3],
    "name": ["Alice", "Bob", "Charlie"]
})

try:
    # Option 1: Pass the engine directly
    df.to_sql("test_table", engine, if_exists="replace", index=False)
    
    print("Success: Data inserted")
except Exception as e:
    print("Error:", e)
