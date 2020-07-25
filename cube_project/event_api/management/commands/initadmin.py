import logging
from django.core.management.base import BaseCommand, CommandError

from event_api.utils.constants import Constants as Const
from event_api.services.db_service import DatabaseController
from cube_project.settings import ADMIN_USERNAME

class Command(BaseCommand):
    help = 'Create superuser account'

    def handle(self, *args, **options):
        dbc = DatabaseController()
        res = dbc.create_superuser()
        if res: self.stdout.write(self.style.SUCCESS('Admin User - {} created successfully'.format(ADMIN_USERNAME)))
