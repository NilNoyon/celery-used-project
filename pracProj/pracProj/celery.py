from __future__ import absolut_import, unicode_literals
import os

from celery import celery
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pracProj.settings')

app = Celery('pracProj')
app.conf.enable_utc = False

app.conf.update(timezone = 'Asia/Dhaka')

app.config_from_object(settings, namespace='CELERY')

# celery beat settings

app.autodiscover_tasks()
@app.task(bind=True)
def debug_task(self):
	print('Request : ', self.request)