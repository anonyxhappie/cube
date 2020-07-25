import logging

class NotificationService:
    """
    This class will handle the incoming notification requests
    """

    logger = logging.getLogger(__name__)
    
    def notify(self, userid, message):
        self.logger.info(message)
