from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
from src.extract import extract_data
from src.transform import transform_data
from src.load import load_data

def etl():
    raw_data = extract_data()
    df = transform_data(raw_data)
    load_data(df, "data/processed/products.csv")

with DAG(
    dag_id="etl_pipeline",
    start_date=datetime(2024, 1, 1),
    schedule_interval="@daily",
    catchup=False
) as dag:

    run_etl = PythonOperator(
        task_id="run_etl",
        python_callable=etl
    )
