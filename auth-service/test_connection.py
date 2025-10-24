import os
import psycopg2
import redis
from dotenv import load_dotenv

load_dotenv()

def test_postgres_connection():
    try:
        conn = psycopg2.connect(
            host=os.getenv("POSTGRES_HOST"),
            port=os.getenv("POSTGRES_PORT"),
            user=os.getenv("POSTGRES_USER"),
            password=os.getenv("POSTGRES_PASSWORD"),
            dbname=os.getenv("POSTGRES_DB")
        )
        cursor = conn.cursor()
        cursor.execute("SELECT version();")
        version = cursor.fetchone()
        print(f"✅ Conexión a PostgreSQL exitosa. Versión: {version[0]}")
        cursor.close()
        conn.close()
    except Exception as e:
        print(f"❌ Error al conectar a PostgreSQL: {e}")

def test_redis_connection():
    try:
        r = redis.Redis(
            host=os.getenv("REDIS_HOST"),
            port=int(os.getenv("REDIS_PORT")),
            db=int(os.getenv("REDIS_DB", 0)),
            decode_responses=True
        )
        r.ping()
        print("✅ Conexión a Redis exitosa.")
    except Exception as e:
        print(f"❌ Error al conectar a Redis: {e}")

if __name__ == "__main__":
    print("🔍 Probando conexiones...")
    test_postgres_connection()
    test_redis_connection()