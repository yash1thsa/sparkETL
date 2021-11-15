from airflow import DAG
from airflow.providers.apache.spark.operators.spark_submit import SparkSubmitOperator
from datetime import datetime, timedelta


# Following are defaults which can be overridden later on
default_args = {
    'owner': 'yash',
    'depends_on_past': False,
    'start_date': datetime(2016, 4, 15),
    'email': ['syashwanth87@gmail.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=1),
}

dag = DAG('dag_market_etl', default_args=default_args, schedule_interval=None)

# t1, t2, t3 and t4 are examples of tasks created using operators

market_etl_runner = SparkSubmitOperator(
    task_id='market_etl_runner',
    application='/Users/yashwanthsanthanam/PycharmProjects/sparkETL/main.py',
    total_executor_cores= 4,
    executor_cores=2,
    executor_memory='5g',
    driver_memory='5g',
    name='market_etl_runner',
    conn_id='spark_local',
    py_files='jobs.zip, model.zip',
    files='config.json',
    job='marketETL',
    dag=dag)

market_etl_runner
