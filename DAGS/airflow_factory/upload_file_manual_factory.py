from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import os   

dag = DAG(
    'upload_file_manual_factory',
    description='A DAG to upload a file to a directory',
    schedule_interval=None,
    start_date=datetime(2023, 1, 1),
    catchup=False
)
