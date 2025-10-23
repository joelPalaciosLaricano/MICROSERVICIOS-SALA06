import os
import psycopg2
import redis

POSTGRES_USER = os.getenv("POSTGRES_USER", "devuser")
POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD", "devpass")
POSTGRES_DB = os.getenv("POSTGRES_DB", "main_db")
REDIS_HOST = os.getenv("REDIS_HOST", "redis")
REDIS_PORT = int(os.getenv("REDIS_PORT", "6379"))

print("Probando conexión a PostgreSQL...")
try:
    conn = psycopg2.connect(
        dbname=POSTGRES_DB,
        user=POSTGRES_USER,
        password=POSTGRES_PASSWORD,
        host="postgres"
    )
    print("Conectado a PostgreSQL correctamente.")
    conn.close()
except Exception as e:
    print("Error al conectar a PostgreSQL:", e)

print("\nProbando conexión a Redis...")
try:
    r = redis.Redis(host=REDIS_HOST, port=REDIS_PORT)
    r.ping()
    print("Conectado a Redis correctamente.")
except Exception as e:
    print("Error al conectar a Redis:", e)