from airflow import DAG
from airflow.operators.python import PythonOperator 
from datetime import datetime, timedelta

def say_hello():
    print("Hello from Airflow")

default_args={
    'owner':'airflow',
    'start_date':datetime(2025,8,9),
    'retries':1,
    'retry_delay':timedelta(minutes=1)
}

with DAG('hello_airflow',default_args=default_args,schedule_interval='@daily',catchup=False) as dag:
    task1=PythonOperator(
        task_id='say_hello_task',
        python_callable=say_hello
    )