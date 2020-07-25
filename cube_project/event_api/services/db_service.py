import logging

from django.contrib.auth.models import User

from ..models import Event, EventRules
from ..utils.exceptions import CustomException
from cube_project.settings import ADMIN_USERNAME, ADMIN_EMAIL, ADMIN_PASSWORD

class DatabaseController:

    logger = logging.getLogger(__name__)

    def get_active_event_rules(self):
        try:
            active_events = EventRules.objects.filter(is_active=True)
            self.logger.debug('Active EventRules retrieved from DB')
            return active_events
        except Exception:
            raise CustomException('DATABASE_READ_ERROR')

    def create_event_rule(self, data):
        try:            
            er_objs, created = EventRules.objects.get_or_create(**data)
            self.logger.debug('Event Rule saved in DB')
        except Exception:
            raise CustomException('DATABASE_WRITE_ERROR')

    def create_event(self, data):
        try:
            event = Event(**data)
            event.save()
            self.logger.debug('Event saved in DB')
        except Exception:
            raise CustomException('DATABASE_WRITE_ERROR')

    def create_superuser(self):
        try:
            if User.objects.filter(email=ADMIN_EMAIL).count() == 0:
                admin = User.objects.create_superuser(email=ADMIN_EMAIL, username=ADMIN_USERNAME, password=ADMIN_PASSWORD)
                admin.is_active = True
                admin.is_admin = True
                admin.save()
                self.logger.debug('Admin User - {} created'.format(ADMIN_USERNAME))    
                return True
            else:
                err_msg = 'Admin user already exist'
                print(err_msg)
                self.logger.debug(err_msg)
                return False    

        except Exception:
            raise CustomException('DATABASE_WRITE_ERROR')
