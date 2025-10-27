# Microservicio de Autenticación

Este microservicio proporciona autenticación basada en JWT para aplicaciones, con almacenamiento en PostgreSQL y caché en Redis.

## Tecnologías utilizadas

- Django 5.0
- Django REST Framework 3.15
- JWT (JSON Web Tokens)
- PostgreSQL
- Redis
- Docker

## Endpoints

### Registro de usuarios
- **URL**: `/api/register/`
- **Método**: POST
- **Datos requeridos**: 
  ```json
  {
    "email": "usuario@ejemplo.com",
    "password": "contraseña_segura"
  }
  ```
- **Respuesta exitosa**: Código 201 (Created)

### Obtener token JWT
- **URL**: `/api/token/`
- **Método**: POST
- **Datos requeridos**: 
  ```json
  {
    "email": "usuario@ejemplo.com",
    "password": "contraseña_segura"
  }
  ```
- **Respuesta exitosa**: Código 200 (OK)
  ```json
  {
    "access": "token_de_acceso",
    "refresh": "token_de_refresco"
  }
  ```

### Refrescar token JWT
- **URL**: `/api/token/refresh/`
- **Método**: POST
- **Datos requeridos**: 
  ```json
  {
    "refresh": "token_de_refresco"
  }
  ```
- **Respuesta exitosa**: Código 200 (OK)
  ```json
  {
    "access": "nuevo_token_de_acceso"
  }
  ```

### Obtener información del usuario autenticado
- **URL**: `/api/me/`
- **Método**: GET
- **Headers requeridos**: 
  ```
  Authorization: Bearer token_de_acceso
  ```
- **Respuesta exitosa**: Código 200 (OK)
  ```json
  {
    "id": 1,
    "email": "usuario@ejemplo.com"
  }
  ```

## Ejecución con Docker

Para ejecutar el microservicio:

```bash
docker-compose up -d
```

El servicio estará disponible en http://localhost:8000/

## Migración de la base de datos

Para crear las tablas necesarias en la base de datos:

```bash
docker exec -it auth_service python manage.py migrate
```

## Creación de superusuario

Para crear un superusuario:

```bash
docker exec -it auth_service python manage.py createsuperuser
```