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

while True:
    command = input("Welcome to Assessment DB\nList of commands:\nLIST, INSERT, DELETE and EXIT\n").strip()

    if command == "EXIT":
        connect_to_db().close()
        quit()

    elif command == "LIST":
        get_db_data(connect_to_db())

    elif command == "INSERT":
        print("INSERT: ")

    elif command == "DELETE":
        print("DELETED: ")

    else:
        print(f"Unknown command: '{command}'")