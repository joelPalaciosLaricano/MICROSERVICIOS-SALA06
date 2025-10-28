# Blog Service

Microservicio para gestionar un blog con categorías, autores y posts, implementado con Django y Django REST Framework.

## Características

- API RESTful para gestionar categorías, autores y posts
- Caché con Redis para endpoints específicos
- Logging estructurado en formato JSON
- Endpoint de healthcheck
- Comando para generar datos de ejemplo
- Documentación OpenAPI

## Requisitos

- Python 3.8+
- Docker y Docker Compose
- PostgreSQL
- Redis

## Configuración y Ejecución

### Usando Docker Compose

1. Clonar el repositorio:

```bash
git clone <repositorio>
cd blog-service
```

2. Iniciar los servicios con Docker Compose:

```bash
docker-compose up -d
```

3. El servicio estará disponible en `http://localhost:8000/api/v1/`

### Desarrollo Local

1. Crear un entorno virtual:

```bash
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
```

2. Instalar dependencias:

```bash
pip install -r requirements.txt
```

3. Configurar variables de entorno:

```bash
export DJANGO_SECRET_KEY='your-secret-key'
export DJANGO_DEBUG=True
export DATABASE_URL='postgresql://user:password@localhost:5432/blog_db'
export REDIS_URL='redis://localhost:6379/0'
```

4. Ejecutar migraciones:

```bash
python manage.py migrate
```

5. Generar datos de ejemplo:

```bash
python manage.py seed_data
```

6. Iniciar el servidor de desarrollo:

```bash
python manage.py runserver
```

## Estructura del Proyecto

```
blog_service/
├── app/
│   ├── categories/       # App para gestionar categorías
│   ├── authors/          # App para gestionar autores
│   ├── posts/            # App para gestionar posts
│   └── core/             # Funcionalidades compartidas
├── blog_service/         # Configuración principal del proyecto
├── docker-compose.yml    # Configuración de Docker Compose
├── Dockerfile            # Configuración de Docker
├── requirements.txt      # Dependencias del proyecto
└── openapi.yaml          # Documentación de la API
```

## API Endpoints

### Categorías

- `GET /api/v1/categories/` - Listar todas las categorías activas

### Posts

- `GET /api/v1/posts/` - Listar todos los posts publicados
  - Parámetros de consulta:
    - `search`: Buscar posts por título o contenido
- `GET /api/v1/posts/{id}/` - Obtener detalle de un post específico

### Sistema

- `GET /api/v1/healthz` - Verificar el estado del servicio

## Ejemplos de Uso

### Listar Categorías

```bash
curl -X GET http://localhost:8000/api/v1/categories/
```

Respuesta:
```json
[
  {
    "id": 1,
    "name": "Tecnología",
    "slug": "tecnologia"
  },
  {
    "id": 2,
    "name": "Ciencia",
    "slug": "ciencia"
  }
]
```

### Buscar Posts

```bash
curl -X GET "http://localhost:8000/api/v1/posts/?search=productividad"
```

Respuesta:
```json
[
  {
    "id": 1,
    "title": "Cómo mejorar tu productividad",
    "slug": "como-mejorar-tu-productividad",
    "excerpt": "En este artículo exploraremos técnicas para mejorar tu productividad diaria...",
    "author": {
      "id": 1,
      "display_name": "Juan Pérez",
      "email": "juan.perez@example.com"
    },
    "category": {
      "id": 1,
      "name": "Tecnología",
      "slug": "tecnologia"
    },
    "published_at": "2023-05-15T14:30:00Z",
    "views": 1250
  }
]
```

### Obtener Detalle de un Post

```bash
curl -X GET http://localhost:8000/api/v1/posts/1/
```

Respuesta:
```json
{
  "id": 1,
  "title": "Cómo mejorar tu productividad",
  "slug": "como-mejorar-tu-productividad",
  "excerpt": "En este artículo exploraremos técnicas para mejorar tu productividad diaria...",
  "body": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam auctor, nisl eget ultricies tincidunt...",
  "author": {
    "id": 1,
    "display_name": "Juan Pérez",
    "email": "juan.perez@example.com"
  },
  "category": {
    "id": 1,
    "name": "Tecnología",
    "slug": "tecnologia"
  },
  "published_at": "2023-05-15T14:30:00Z",
  "views": 1251
}
```

### Verificar Estado del Servicio

```bash
curl -X GET http://localhost:8000/api/v1/healthz
```

Respuesta:
```json
{
  "status": "ok",
  "database": "ok",
  "cache": "ok"
}
```

## Comandos Útiles

### Generar Datos de Ejemplo

```bash
# Dentro del contenedor Docker
docker-compose exec web python manage.py seed_data

# O localmente
python manage.py seed_data --categories 5 --authors 10 --posts 50
```

### Ejecutar Pruebas

```bash
# Dentro del contenedor Docker
docker-compose exec web python manage.py test

# O localmente
python manage.py test
```