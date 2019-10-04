
from __future__ import print_function

import time
from builtins import range
from pprint import pprint

import airflow
from airflow.models import DAG
from airflow.operators.python_operator import PythonOperator

args = {
    'owner': 'airflow',
    'start_date': airflow.utils.dates.days_ago(2),
}

dag = DAG(
    dag_id='my_print',
    default_args=args,
    schedule_interval=None,
)

def my_print(ds, **kwargs):
   print("TEST")


run_this = PythonOperator(
    task_id='my_print_task',
    provide_context=True,
    python_callable=my_print,
    dag=dag,
)

run_this
