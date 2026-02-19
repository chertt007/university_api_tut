import psycopg2

from psycopg2.extras import RealDictCursor

from app.config import settings


def get_db_connection():
    conn = psycopg2.connect(
        host=settings.DATABASE_HOST,
        dbname=settings.DATABASE_NAME,
        user=settings.DATABASE_USER,
        password=settings.DATABASE_PASSWORD,
    )
    cursor = conn.cursor(cursor_factory=RealDictCursor)
    return conn, cursor
