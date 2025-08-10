import sys
sys.path.insert(0, '/opt/airflow/scripts') 
from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.email import EmailOperator
import datetime as dt
import main

default_args = {
    "owner": "Airflow_Dilshad",
    "retries": 1,
    "start_date": dt.datetime(2025, 8, 10),
    'retry_delay': dt.timedelta(minutes=5),
    'email': ['dilshadahmed.de@gmail.com']
}

dag = DAG(
    "telecom_etl_dag",
    default_args=default_args,
    schedule_interval=''0 */1 * * *'',
    catchup=False
)

task1 = PythonOperator(
    task_id='python_task',
    python_callable=main.run_once,
    dag=dag,
)


task1 
