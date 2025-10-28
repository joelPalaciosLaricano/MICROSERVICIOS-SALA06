from django.core.cache import cache
from functools import wraps
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page

def get_cache_key(prefix, *args, **kwargs):
    """Genera una clave de caché única basada en los argumentos"""
    key_parts = [prefix]
    key_parts.extend([str(arg) for arg in args])
    key_parts.extend([f"{k}:{v}" for k, v in sorted(kwargs.items())])
    return ":".join(key_parts)

def cache_response(timeout=60):
    """Decorador para cachear respuestas de API"""
    def decorator(view_func):
        @wraps(view_func)
        def _wrapped_view(self, request, *args, **kwargs):
            return cache_page(timeout)(view_func)(self, request, *args, **kwargs)
        return _wrapped_view
    return decorator