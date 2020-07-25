from __future__ import annotations
from abc import ABC, abstractmethod

import json
import logging
from datetime import datetime, timedelta

from django.db.models import Q

from ..tasks import celery_task
from ..models import Event
from ..utils.utilities import Utilities as Util
from ..utils.constants import Constants as Const
from .notification_service import NotificationService

class Rule(ABC):
    """
    The Rule interface declares operations common to all supported versions
    of some algorithm.

    The Context uses this interface to call the algorithm defined by Event
    Rules.
    """

    @abstractmethod
    def execute(self, data):
        pass


"""
Event Rules implement the algorithm while following the base Rule
interface. The interface makes them interchangeable in the Context.
"""


class EventRule(Rule):
    """
    This class is created for initial Context object.
    """

    def execute(self, data):
        pass

class EventRuleA(Rule):

    logger = logging.getLogger(__name__)
    
    def execute(self, data):
        """
        Trigger a push notification on very first bill pay event for the user
        """
        bill_pay_events_count = Event.objects.filter(Q(userid=data.get(Const.USERID)) & Q(noun=Const.BILL) & Q(verb=Const.PAY)).count()
        if (bill_pay_events_count == 1):
            ns = NotificationService()
            ns.notify(data.get(Const.USERID), Const.NOTIFY_TEXT_DICT['EventRuleA'])
            return True

        return False
        
class EventRuleB(Rule):

    logger = logging.getLogger(__name__)

    def execute(self, data):
        """
        Alert user if 5 or more bill pay events of total value >= 20000 
        happen within 5 minutes timewindow
        """
        five_minutes_ago = str(datetime.now() + timedelta(minutes=-5))
        five_minutes_ago = Util.get_modified_date(five_minutes_ago)

        bill_pay_events = Event.objects.filter(Q(userid=data.get(Const.USERID)) & Q(noun=Const.BILL) & Q(verb=Const.PAY) & Q(ts__gt=five_minutes_ago))
        
        if (len(bill_pay_events) >= 5):
            total_bill_pay = 0
            for bill_pay_event in bill_pay_events:
                properties = json.loads(bill_pay_event.properties)
                total_bill_pay += properties.get(Const.VALUE)
                if (total_bill_pay >= Const.BILL_PAY_LIMIT): 
                    ns = NotificationService()
                    ns.notify(data.get(Const.USERID), Const.NOTIFY_TEXT_DICT['EventRuleB'])
                    return True

        return False

class EventRuleC(Rule):

    logger = logging.getLogger(__name__)

    def execute(self, data):
        """
        Alert cube operator if bill paid, 
        but did not give feedback within 15 minutes of the bill pay event
        """
        if (data.get(Const.NOUN) == Const.BILL and data.get(Const.VERB) == Const.PAY):
            celery_task.delay(data)
            debug_text = 'Background job triggered'
            self.logger.debug(debug_text)
            return True

        return False
        

class Context():
    """
    The Context defines the interface of interest to clients.
    """

    def __init__(self, rule: Rule):
        """
        Usually, the Context accepts a rule through the constructor, but
        also provides a setter to change it at runtime.
        """

        self._rule = rule

    @property
    def rule(self):
        """
        The Context maintains a reference to one of the Rule objects. The
        Context does not know the concrete class of a rule. It should work
        with all strategies via the Rule interface.
        """

        return self._rule

    @rule.setter
    def rule(self, rule: Rule):
        """
        Usually, the Context allows replacing a Rule object at runtime.
        """

        self._rule = rule

    def apply_trigger_rule(self, data):
        """
        The Context delegates some work to the Rule object instead of
        implementing multiple versions of the algorithm on its own.
        """

        # ...

        # print("Context: executing trigger as per the rule (not sure how it'll do it)")
        result = self._rule.execute(data)
        # print("result", result)

        # ...

