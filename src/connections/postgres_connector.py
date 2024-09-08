import psycopg2

def connect_to_database():
    return psycopg2.connect(
        host="localhost",
        user="root",
        password="krish123",
        database="a02"
    )
