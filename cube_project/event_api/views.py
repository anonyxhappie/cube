import sys
import logging
import traceback
from datetime import datetime

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Event
from .serializers import EventSerializer
from .utils.utilities import Utilities as Util
from .utils.constants import Constants as Const
from .utils.exceptions import CustomException
from .services.event_service import EventHandlerService

class TriggerEventView(APIView):

    logger = logging.getLogger(__name__)

    def post(self, request):
        """
            With assumption that API request authorization is checked on API Gateway
            Can validate for permissions (to trigger) here if receiving in request header 
        """
        try:
            request_data = request.data
            request_data[Const.TIMESTAMP] = Util.get_modified_date(str(datetime.now()))
            _serializer = EventSerializer(data=request_data)
            if (_serializer.is_valid()):
                self.logger.debug('An event triggered by {}'.format(request_data.get('userid')))
                ehs = EventHandlerService()
                ehs.event_handler(request_data)
                self.logger.debug('Event handled successfully')
            else:
                raise CustomException('INVALID_REQUEST')
            return Response({
                Const.STATUS: status.HTTP_200_OK,
                Const.MESSAGE: 'Event triggered.'
            })
        except CustomException as e:
            traceback.print_exc()
            return Response({
                Const.STATUS: e.error_code,
                Const.MESSAGE: e.error_message
            })
        except Exception as e:
            traceback.print_exc()
            self.logger.exception('Internal Server Error')
            return Response({
                Const.STATUS: status.HTTP_500_INTERNAL_SERVER_ERROR,
                Const.MESSAGE: 'Something went wrong. Please contact support team.'
            })
