import time
import logging
from datetime import datetime, timedelta

from django.db.models import Q
from .models import Event
from .utils.constants import Constants as Const
from .services.notification_service import NotificationService

from celery import shared_task

@shared_task
def celery_task(data):
    """
    Background task to alert cube operator if bill paid, 
    but did not give feedback within 15 minutes of the bill pay event
    """
    logger = logging.getLogger(__name__)

    minutes = Const.FEEDBACK_TIME_LIMIT * 60
    time.sleep(minutes)
    
    fdbk_post_events_count = Event.objects.filter(
        Q(userid=data.get(Const.USERID)) 
        & Q(noun=Const.FEEDBACK) 
        & Q(verb=Const.POST) 
        & Q(ts__gt=data.get(Const.TIMESTAMP))).count()

    if (fdbk_post_events_count < 1):
        ns = NotificationService()
        ns.notify(data.get(Const.USERID), Const.NOTIFY_TEXT_DICT['EventRuleC'])
        return True

    feedback_text = 'Feedback Received.'
    logger.debug(feedback_text)
    return False
