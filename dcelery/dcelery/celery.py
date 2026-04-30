import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dcelery.settings')

app = Celery("dcelery")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.conf.task_routes = {
    'newapp.tasks.mul': {'queue': 'queue1'},
    'nweapp.tasks.div': {'queue': 'queue2'},
    'newapp.tasks.sub': {'queue': 'queue2'},
}
app.autodiscover_tasks()


@app.task
def add_numbers(a: int, b: int):
    """ To add two numbers"""
    return a+b