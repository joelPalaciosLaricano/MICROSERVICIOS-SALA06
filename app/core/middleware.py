import json
import time
import logging
from django.utils.deprecation import MiddlewareMixin

logger = logging.getLogger('blog_service')

class LoggingMiddleware(MiddlewareMixin):
    """
    Middleware para registrar información de cada solicitud en formato JSON.
    """
    def process_request(self, request):
        request.start_time = time.time()
        return None

    def process_response(self, request, response):
        if hasattr(request, 'start_time'):
            duration = time.time() - request.start_time
            status_code = response.status_code
            
            log_data = {
                'method': request.method,
                'path': request.path,
                'status': status_code,
                'duration': round(duration * 1000, 2),  # en milisegundos
            }
            
            # Añadir información adicional si está disponible
            if hasattr(request, 'user') and request.user.is_authenticated:
                log_data['user'] = request.user.username
            
            logger.info(
                f"Request processed",
                extra={
                    'method': request.method,
                    'path': request.path,
                    'status': status_code,
                    'duration': round(duration * 1000, 2)
                }
            )
        
        return response

class AuthHeaderMiddleware(MiddlewareMixin):
    """
    Middleware para capturar y registrar el header de autorización.
    Este es un esqueleto que se conectará al servicio de Auth en el futuro.
    """
    def process_request(self, request):
        auth_header = request.headers.get('Authorization')
        if auth_header and auth_header.startswith('Bearer '):
            token = auth_header.split(' ')[1]
            # Solo registramos que recibimos un token, sin validarlo todavía
            logger.info(
                f"Received authorization token",
                extra={
                    'token_received': True,
                    'path': request.path,
                }
            )
            # Aquí se implementará la validación del token en el futuro
            request.auth_token = token
        
        return None