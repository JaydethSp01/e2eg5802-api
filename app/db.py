import os
import psycopg

DATABASE_URL = os.environ.get("DATABASE_URL")

if DATABASE_URL:
    conn = psycopg.connect(DATABASE_URL)
else:
    conn = None

# Function to initialize the database

if conn:
    def init_db():
        with conn.cursor() as cur:
            cur.execute("CREATE TABLE IF NOT EXISTS clientes (id SERIAL PRIMARY KEY, nombre VARCHAR(100), telefono VARCHAR(20), email VARCHAR(100));")
            cur.execute("CREATE TABLE IF NOT EXISTS citas (id SERIAL PRIMARY KEY, cliente_id INT, barbero_id INT, fecha TIMESTAMP, FOREIGN KEY (cliente_id) REFERENCES clientes (id), FOREIGN KEY (barbero_id) REFERENCES barberos (id));")
            # More tables...
        conn.commit()

    init_db()
else:
    print("Running in mock mode")