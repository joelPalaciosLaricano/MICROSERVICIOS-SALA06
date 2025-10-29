import time
import logging
import json
from django.utils.deprecation import MiddlewareMixin

logger = logging.getLogger(__name__)

class RequestLoggingMiddleware(MiddlewareMixin):
    def process_request(self, request):
        request._start_time = time.time()

    def process_response(self, request, response):
        try:
            took = (time.time() - getattr(request, '_start_time', time.time()))
        except Exception:
            took = 0
        payload = {
            'method': request.method,
            'path': request.get_full_path(),
            'status': getattr(response, 'status_code', 0),
            'time': round(took, 4)
        }
        logger.info(json.dumps(payload))
        return response

class AuthHeaderLoggingMiddleware(MiddlewareMixin):
    """Skeleton middleware: logs Authorization header if present. Does not validate."""
    def process_request(self, request):
        auth = request.META.get('HTTP_AUTHORIZATION')
        if auth:
            logger.info(json.dumps({'auth_header': auth[:200]}))
