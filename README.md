# 🧠 Blog Service — Django + PostgreSQL + Redis + Docker

Microservicio base del sistema de blog, desarrollado con **Django 5**, **Django REST Framework**, **PostgreSQL**, y **Redis**.  
Este servicio expone endpoints públicos para listar categorías y posts, además de incluir caché, paginación, búsqueda y health check.

---

## 🚀 Tecnologías principales

- **Python 3.11**
- **Django 5.0**
- **Django REST Framework 3.15**
- **PostgreSQL 13**
- **Redis 6**
- **Docker Compose**
- **Gunicorn**
- **django-redis**
- **django-filter**

---

## ⚙️ Estructura del proyecto

blog-service/
│
├── app/
│ ├── blog_service/ # Proyecto Django principal
│ ├── core/ # Utilidades (cache, paginación)
│ ├── categories/ # App de categorías
│ ├── authors/ # App de autores
│ ├── posts/ # App de posts
│ ├── manage.py
│
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── openapi.yaml

---

## 🐳 Configuración con Docker

El proyecto se ejecuta completamente dentro de contenedores Docker.

### 1️⃣ Construir e iniciar los servicios

Desde la raíz del proyecto:

```bash

Esto levantará los siguientes servicios:

docker compose up --build

| Servicio       | Puerto local | Descripción             |
| -------------- | ------------ | ----------------------- |
| `postgres`     | 5432         | Base de datos principal |
| `redis`        | 6379         | Caché                   |
| `blog_service` | 8001         | API Django              |

⚙️ Variables de entorno

Las variables de entorno básicas están definidas en el docker-compose.yml:

environment:
  - DB_HOST=postgres
  - DB_NAME=main_db
  - DB_USER=devuser
  - DB_PASS=devpass
  - REDIS_HOST=redis
  - REDIS_PORT=6379
  - DEBUG=1

🧩 Migraciones y carga inicial de datos

Una vez que los contenedores estén corriendo:

# Entrar al contenedor Django
docker compose exec blog bash

# Ejecutar migraciones
python manage.py migrate

# Cargar datos iniciales (categorías, autores, posts)
python manage.py seed_blog

🌐 Endpoints disponibles
Método	Endpoint	Descripción
GET	/api/categories/	Lista categorías activas
GET	/api/posts/	Lista paginada y filtrable de posts publicados
GET	`/api/posts/{id	slug}/`
GET	/healthz/	Verifica conexión a DB y Redis
🧭 Características técnicas

🔍 Paginación por defecto de 10 elementos (PAGE_SIZE=10)

🔎 Búsqueda simple (?search= sobre title o body)

⚡ Caché Redis para:

GET /api/categories/

GET /api/posts/{id|slug}/

🧱 Middleware esqueleto para lectura de header Authorization: Bearer ...

📈 Logging estructurado (JSON) con método, path, estado y tiempo

🧰 Healthcheck /healthz que valida conexión DB y Redis

🧪 Ejemplos de prueba

Obtener categorías:

curl http://localhost:8001/api/categories/


Obtener lista de posts:

curl http://localhost:8001/api/posts/?search=django&page=1


Ver detalle de un post:

curl http://localhost:8001/api/posts/1/


Verificar estado del servicio:

curl http://localhost:8001/healthz/

🧱 Contrato OpenAPI

El archivo openapi.yaml documenta los endpoints principales y sus respuestas esperadas.
Este contrato puede ser utilizado por el equipo Frontend para la integración inicial.

🧑‍💻 Autor

Desarrollado por Emer, como parte del microservicio base para la arquitectura del blog.
Versión inicial (MVP) con endpoints públicos, caché, healthcheck y logging estructurado.

🧰 Comandos útiles
# Construir e iniciar contenedores
docker compose up --build

# Detener contenedores
docker compose down

# Ver logs en tiempo real
docker compose logs -f blog

# Entrar al contenedor Django
docker compose exec blog bash

# Crear superusuario (opcional)
python manage.py createsuperuser

📄 Licencia

MIT License © 2025
Libre para uso educativo y desarrollo personal.
