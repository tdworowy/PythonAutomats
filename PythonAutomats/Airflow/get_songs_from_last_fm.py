
from __future__ import print_function

import time
from builtins import range
from pprint import pprint

import airflow
from Songs.last_fm_parser import get_titles,get_pages_count
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
def get_titles_for_user(user):
    url = 'https://www.last.fm/pl/user/%s/library/tracks' % user
    titles_map = map(get_titles, [url + '?page= %s' % str(i) for i in range(1, get_pages_count(user) + 1)])
    titles = list(titles_map)
    print(titles)
    return titles




for user in ["TotaledThomas","TheRoobal"]:
    task = PythonOperator(
        task_id='%s_songs' % user,
        python_callable=get_titles_for_user,
        op_kwargs={'user': user},
        dag=dag,
    )

task
