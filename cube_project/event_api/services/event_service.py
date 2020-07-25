import sys
import json
import logging
from datetime import datetime

from ..models import Event, EventRules
from ..utils.constants import Constants as Const
from .db_service import DatabaseController
from .rule_service import Context, EventRule, EventRuleA, EventRuleB, EventRuleC

class EventHandlerService:

    logger = logging.getLogger(__name__)

    def __init__(self):
        self.dbc = DatabaseController()

    def event_handler(self, data):
        temp_data = data
        temp_data[Const.PROPERTIES] = json.dumps(temp_data.get(Const.PROPERTIES))
        self.dbc.create_event(temp_data)

        active_event_rules = self.dbc.get_active_event_rules()
        context = Context(EventRule())

        for event_rule in active_event_rules:
            class_name = event_rule.rule_name
            self.logger.debug('applying {}'.format(class_name))
            context.rule = self.str_to_class(class_name)()
            context.apply_trigger_rule(data)
        
        return True

    def str_to_class(self, classname):
        return getattr(sys.modules[__name__], classname)