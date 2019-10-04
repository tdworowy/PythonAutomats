
from __future__ import print_function

import time
from builtins import range
from pprint import pprint

import airflow
from Songs.last_fm_parser import get_titles
from airflow.models import DAG
from airflow.operators.python_operator import PythonOperator

args = {
    'owner': 'airflow',
    'start_date': airflow.utils.dates.days_ago(2),
}

dag = DAG(
    dag_id='get_songs_from_last_fm',
    default_args=args,
    schedule_interval=None,
)

def get_songs(ds, **kwargs):
    get_titles('https://www.last.fm/pl/user/TotaledThomas/library/tracks')
    get_titles('https://www.last.fm/pl/user/TheRoobal/library/tracks')


run_this = PythonOperator(
    task_id='get_songs_from_last_fm',
    provide_context=True,
    python_callable=get_songs,
    dag=dag,
)

run_this
