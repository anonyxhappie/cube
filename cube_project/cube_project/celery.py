import os
import logging
from celery import Celery
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cube_project.settings')
app = Celery('djangocelery')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()
logger = logging.getLogger(__name__)
logger.info('Celery configured successfully.')