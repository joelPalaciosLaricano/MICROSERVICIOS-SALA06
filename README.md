# MICROSERVICIOS-SALA06
# Laboratorio de Microservicios (Django + React)

## Arquitectura inicial
- **auth-service/**       → Autenticación y tokens JWT
- **blog-service/**       → Publicaciones, autores y categorías
- **email-service/**     → Notificaciones y formularios (envío de correos)
- **frontend/**           → Interfaz de usuario construida con React
- **reverse-proxy/**     → Balanceo de carga y Gateway local 

**Servicios base compartidos:**
- **PostgreSQL** (5432) - Base de datos principal.
- **Redis** (6379) - Caché y gestión de sesiones/tokens.
