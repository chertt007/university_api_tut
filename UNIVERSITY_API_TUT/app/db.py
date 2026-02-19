import os

import psycopg2
from psycopg2.extras import RealDictCursor


def get_db_connection():
    db_host = os.getenv("DATABASE_HOST", os.getenv("POSTGRES_HOST", "localhost"))
    db_name = os.getenv("DATABASE_NAME", os.getenv("POSTGRES_DB"))
    db_user = os.getenv("DATABASE_USER", os.getenv("POSTGRES_USER"))
    db_password = os.getenv("DATABASE_PASSWORD", os.getenv("POSTGRES_PASSWORD"))

    conn = psycopg2.connect(
        host=db_host,
        dbname=db_name,
        user=db_user,
        password=db_password,
    )
    cursor = conn.cursor(cursor_factory=RealDictCursor)
    return conn, cursor
