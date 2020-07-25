import logging
from django.core.management.base import BaseCommand, CommandError
from event_api.utils.constants import Constants as Const
from event_api.services.db_service import DatabaseController

class Command(BaseCommand):
    help = 'Add default event rules in database'

    logger = logging.getLogger(__name__)

    def handle(self, *args, **options):
        
        dbc = DatabaseController()
        for rule in Const.DEFAULT_EVENT_RULES:
            data = {
                Const.RULE_NAME: rule,
                Const.RULE_DESCRIPTION: Const.DEFAULT_EVENT_RULES[rule],
            }
            dbc.create_event_rule(data)
        self.logger.debug('Default event rules added')    
        self.stdout.write(self.style.SUCCESS('Default event rules added successfully'))