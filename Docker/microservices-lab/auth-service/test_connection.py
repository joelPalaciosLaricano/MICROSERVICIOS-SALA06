import os
import sys
import psycopg2
import redis
from dotenv import load_dotenv

# Cargar variables de entorno
load_dotenv()

def test_postgres_connection():
    """Prueba la conexión a PostgreSQL"""
    try:
        conn = psycopg2.connect(
            dbname=os.getenv("POSTGRES_DB", "main_db"),
            user=os.getenv("POSTGRES_USER", "devuser"),
            password=os.getenv("POSTGRES_PASSWORD", "devpass"),
            host="postgres",
            port="5432"
        )
        print("✅ Conexión a PostgreSQL exitosa!")
        conn.close()
        return True
    except Exception as e:
        print(f"❌ Error al conectar a PostgreSQL: {e}")
        return False

def test_redis_connection():
    """Prueba la conexión a Redis"""
    try:
        r = redis.Redis(
            host=os.getenv("REDIS_HOST", "redis"),
            port=int(os.getenv("REDIS_PORT", 6379)),
            decode_responses=True
        )
        r.ping()
        print("✅ Conexión a Redis exitosa!")
        return True
    except Exception as e:
        print(f"❌ Error al conectar a Redis: {e}")
        return False

if __name__ == "__main__":
    print("Probando conexiones a servicios...")
    pg_success = test_postgres_connection()
    redis_success = test_redis_connection()
    
    if pg_success and redis_success:
        print("🎉 Todas las conexiones funcionan correctamente!")
        sys.exit(0)
    else:
        print("⚠️ Algunas conexiones fallaron. Revisa la configuración.")
        sys.exit(1)