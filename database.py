import psycopg2

def get_connection():
    return psycopg2.connect(
        dbname = "feeding_db",
        user = "nathan",
        password = "Nathan84110333!",
        host = "localhost",
        port = "5432",
    )

def create_table():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS usuarios (
            id SERIAL PRIMARY KEY,
            user_id_input TEXT,
            nome TEXT UNIQUE
        )    
    """)
    conn.commit()
    cur.close()
    conn.close()