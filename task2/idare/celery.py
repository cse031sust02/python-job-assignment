import os
import time

from celery import Celery


# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'idare.settings')

app = Celery('idare')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()


@app.task
def task_1():
    print('Task 1 is sleeping for two seconds')
    time.sleep(2)
    return


@app.task
def task_2():
    print('Task 2 is sleeping for three seconds')
    time.sleep(3)
    return


app.conf.beat_schedule = {
    'task 1': {
        'task': 'task_1.s',
        'schedule': 1
    },
    'task 2': {
        'task': 'task_2.s',
        'schedule': 1
    },
}
