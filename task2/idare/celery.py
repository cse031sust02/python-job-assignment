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


@app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    # run in every second
    sender.add_periodic_task(1.0, task_1.s(), name='task 1')
    sender.add_periodic_task(1.0, task_2.s(), name='task 2')
