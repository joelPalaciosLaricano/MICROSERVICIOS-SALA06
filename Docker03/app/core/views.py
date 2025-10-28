from django.db import connection
from django.core.cache import cache
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class HealthCheckView(APIView):
    """
    Endpoint para verificar la salud del servicio.
    Comprueba la conexión a la base de datos y a Redis.
    """
    def get(self, request):
        health_status = {
            'status': 'ok',
            'database': 'ok',
            'cache': 'ok'
        }
        
        # Verificar conexión a la base de datos
        try:
            with connection.cursor() as cursor:
                cursor.execute("SELECT 1")
                cursor.fetchone()
        except Exception as e:
            health_status['database'] = 'error'
            health_status['status'] = 'error'
        
        # Verificar conexión a Redis
        try:
            cache.set('healthcheck', 'ok', 10)
            result = cache.get('healthcheck')
            if result != 'ok':
                raise Exception("Cache check failed")
        except Exception as e:
            health_status['cache'] = 'error'
            health_status['status'] = 'error'
        
        status_code = status.HTTP_200_OK if health_status['status'] == 'ok' else status.HTTP_503_SERVICE_UNAVAILABLE
        
        return Response(health_status, status=status_code)