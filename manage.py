#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
    # Configuración para asegurar que Django funcione correctamente en Docker
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'blog_service.settings')
    # Asegurarse que Django pueda escuchar en todas las interfaces de red en Docker
    os.environ.setdefault('DJANGO_ALLOWED_HOSTS', '*')
    # Configurar la base de datos para Docker si es necesario
    if os.environ.get('DATABASE_URL'):
        os.environ.setdefault('DATABASE_ENGINE', 'django.db.backends.postgresql')
    
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()