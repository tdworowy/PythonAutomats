
from __future__ import print_function

import time
from builtins import range
from pprint import pprint

import airflow
from Songs.last_fm_parser import get_titles,get_pages_count,tag_song
from airflow.models import DAG
from airflow.operators.python_operator import PythonOperator

users = ["TotaledThomas","TheRoobal"]

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
    #last_page = get_pages_count(user) + 1
    last_page = 2
    titles_map = map(get_titles, [url + '?page= %s' % str(i) for i in range(1, last_page)])
    titles = list(titles_map)
    return titles

def tag_songs(**kwargs):
    task_instance = kwargs['task_instance']
    task_ids=['%s_songs' % user for user in users]
    arguments = task_instance.xcom_pull(task_ids=task_ids)

    _new_list = []
    for element in arguments:
        _new_list.extend(element)

    _new_dic = {}
    for _dic in _new_list:
        _new_dic.update(_dic)

    return list(map(lambda tuple: tag_song(tuple[0], tuple[1]), _new_dic.items()))

task_tag_songs = PythonOperator(task_id='Tag_songs',
                          provide_context=True,
                          python_callable=tag_songs, dag=dag)

for user in users:
    task = PythonOperator(
        task_id='%s_songs' % user,
        python_callable=get_titles_for_user,
        op_kwargs={'user': user},
        dag=dag,
    )

task >> task_tag_songs
