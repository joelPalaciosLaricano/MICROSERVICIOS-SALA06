from django.db import connections
from django.db import DEFAULT_DB_ALIAS
from django_redis import get_redis_connection
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer, BrowsableAPIRenderer
from rest_framework.response import Response


@api_view(['GET'])
@renderer_classes([JSONRenderer, BrowsableAPIRenderer])
def healthz(request):
    """Health check that returns JSON for machines and a browsable page for humans."""
    # Check DB
    db_ok = False
    try:
        c = connections[DEFAULT_DB_ALIAS]
        c.cursor()
        db_ok = True
    except Exception:
        db_ok = False

    # Check Redis
    redis_ok = False
    try:
        rc = get_redis_connection("default")
        rc.ping()
        redis_ok = True
    except Exception:
        redis_ok = False

    status_code = 200 if db_ok and redis_ok else 503
    payload = {
        'status': 'ok' if db_ok and redis_ok else 'degraded',
        'database': 'ok' if db_ok else 'fail',
        'cache': 'ok' if redis_ok else 'fail',
    }
    return Response(payload, status=status_code)
