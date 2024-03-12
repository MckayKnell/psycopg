import os
import psycopg2

database_name = os.environ.get("DATABASE_NAME")

conn = psycopg2.connect(f'dbname={database_name}')

cursor = conn.cursor()


def create_all():
    print("creating tables...")

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Products (
    product_id SERIAL PRIMARY KEY,
    product_name VARCHAR NOT NULL UNIQUE,
    description VARCHAR,
    price FLOAT,
    active BOOLEAN DEFAULT true
    );
    """)
    conn.commit()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Companies (
    company_id SERIAL PRIMARY KEY,
    company_name VARCHAR NOT NULL UNIQUE
    );
    """)
    conn.commit()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Categories (
    category_id SERIAL PRIMARY KEY,
    category_name VARCHAR NOT NULL UNIQUE
    );
    """)
    conn.commit()
    print("Table created")
