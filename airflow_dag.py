from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
import os

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2024, 5, 10),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG(
    'data_pipeline',
    default_args=default_args,
    description='A DAG to automate data extraction, transformation, and storage',
    schedule_interval=timedelta(days=1),
)

# Define Python functions for each task
def extract_data():
    os.system('python extract_data.py')

def preprocess_data():
    os.system('python preprocess_data.py')

def save_to_json():
    os.system('python save_to_json.py')

# Define tasks for each step in the data pipeline
extract_task = PythonOperator(
    task_id='extract_data',
    python_callable=extract_data,
    dag=dag,
)

preprocess_task = PythonOperator(
    task_id='preprocess_data',
    python_callable=preprocess_data,
    dag=dag,
)

save_task = PythonOperator(
    task_id='save_to_json',
    python_callable=save_to_json,
    dag=dag,
)

# Define task dependencies
extract_task >> preprocess_task >> save_task
