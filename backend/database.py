import psycopg2

def get_db_connection():
    # Sustituye con tus datos de pgAdmin
    conn = psycopg2.connect(
        host="localhost",
        database="taskcampus",
        user="postgres",
        password="Spike"
    )
    return conn