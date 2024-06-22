from celery import Celery
import os
import time
from django.conf import settings


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'devlearn.settings')

app = Celery('devlearn')
app.config_from_object('django.conf:settings')
app.conf.broker_url = settings.CELERY_BROKER_URL
app.autodiscover_tasks()


@app.task()
def debug_task(): # debug_task() or debug_task.delay()
    time.sleep(2)
    print('Hello form debug_task')
