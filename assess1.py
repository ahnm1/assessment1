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

def get_db_data(connection):
    list_all = "SELECT * FROM view_contacts;"
    cursor = connection.cursor()
    cursor.execute(list_all, )
    fetch_all = cursor.fetchall()
    cursor.close()
    for item in fetch_all:
        print(item)

    return fetch_all

get_db_data(connect_to_db())