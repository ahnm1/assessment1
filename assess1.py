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
    list_all = "SELECT * FROM contacts;"
    cursor = connection.cursor()
    cursor.execute(list_all, )
    fetch_all = cursor.fetchall()
    cursor.close()
    for item in fetch_all:
        print(item)

    return fetch_all

def add_contact(connection, id_number, first_name, last_name, title, organization):
    add_to = f"INSERT INTO contacts VALUES ({id_number}, '{ first_name }','{ last_name }', '{ title }', '{ organization }');"
    cursor = connection.cursor()
    cursor.execute(add_to, (first_name, last_name, title, organization))
    connection.commit()
    cursor.close()


while True:
    command = input("Welcome to Assessment DB\nList of commands:\nLIST, INSERT, DELETE and EXIT\n").strip()

    if command == "EXIT":
        connect_to_db().close()
        quit()

    elif command == "LIST":
        print("- LIST -")
        get_db_data(connect_to_db())

    elif command == "INSERT":
        id_number    = input("Id number: ").strip()
        first_name   = input("First name: ").strip()
        last_name    = input("Last name: ").strip()
        title        = input("Title: ").strip()
        organization = input("Organization: ").strip()

        add_contact(connect_to_db(), id_number, first_name, last_name, title, organization)

    elif command == "DELETE":
        print("- DELETED -")

    else:
        print(f"Unknown command: '{command}'")