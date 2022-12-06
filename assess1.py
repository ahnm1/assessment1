import psycopg2

DB_PASS = "4231-rweq"

def get_db_connection():
    connection = psycopg2.connect(
        host     = "localhost",
        port     = "5432",
        database = "assessmentdb",
        user     = "postgres",
        password = DB_PASS
        )

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

def delete_contact(connection, id_number):
    del_contact = f"DELETE FROM contacts WHERE id = { id_number };"
    
    cursor = connection.cursor()
    cursor.execute(del_contact, (id_number, ))
    connection.commit()
    cursor.close()
    print(f"- DELETED contact with ID: { id_number } -")


while True:
    command = input("Welcome to Assessment DB\nList of commands:\nLIST, INSERT, DELETE and EXIT\n").strip()

    if command == "EXIT":
        get_db_connection().close()
        quit()

    elif command == "LIST":
        print("- LIST -")
        get_db_data(get_db_connection())

    elif command == "INSERT":
        id_number    = input("Id number: ").strip()
        first_name   = input("First name: ").strip()
        last_name    = input("Last name: ").strip()
        title        = input("Title: ").strip()
        organization = input("Organization: ").strip()

        add_contact(get_db_connection(), id_number, first_name, last_name, title, organization)

    elif command == "DELETE":
        id_number    = input("Id number: ").strip()
        delete_contact(get_db_connection(), id_number)

    else:
        print(f"Unknown command: '{command}'")