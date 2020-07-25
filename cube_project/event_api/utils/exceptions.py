import logging

from .constants import Constants as Const

class CustomException(Exception):
    """Parent exception class for all custom exceptions raised in the project"""

    logger = logging.getLogger(__name__)

    def __init__(self, code='DEFAULT'):
        self.error_code = Const.EXCEPTION_CODES[code][0]
        self.error_message = Const.EXCEPTION_CODES[code][1]
        print(self.error_message)
        self.logger.exception(self.error_message)
