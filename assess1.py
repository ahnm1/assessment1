import psycopg2
DB_PASS = "4231-rweq"

def connect_to_db():
    connection = psycopg2.connect(
        host     = "localhost",
        port     = "5432",
        database = "assessmentdb",
        user     = "postgres",
        password = DB_PASS)
        
    return connection

connect_to_db()