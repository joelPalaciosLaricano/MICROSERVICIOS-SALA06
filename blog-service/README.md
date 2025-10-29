# Blog Service

Microservice (Django + DRF) exposing categories and posts with pagination, search and Redis caching.

Ports: 8001

How to run (Docker compose):

```powershell
# from repository root
docker compose down -v --rmi local
docker compose build
docker compose up -d

# Enter the blog container to run migrations and seed
docker compose exec blog bash
python manage.py migrate
python manage.py seed_blog
```

Endpoints:
- GET /api/categories/ — list active categories (cached)
- GET /api/posts/?search=&page= — list posts (published)
- GET /api/posts/{id|slug}/ — post detail (cached)
- GET /healthz — health check for DB and Redis

Seed: management command `python manage.py seed_blog` creates 5 categories, 3 authors, 30 posts.

OpenAPI: see `openapi.yaml` for minimal contract.

Example cURL:

```bash
curl http://localhost:8001/api/posts/?page=1
curl http://localhost:8001/api/posts/1/
curl http://localhost:8001/api/categories/
curl http://localhost:8001/healthz
```
