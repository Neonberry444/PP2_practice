import csv
from connect import connect_db


connection = connect_db()
cursor = connection.cursor()

# Create table
cursor.execute("""
CREATE TABLE IF NOT EXISTS phonebook (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    phone VARCHAR(20)
)
""")
connection.commit()


# Insert contact manually
def insert_contact(name, phone):
    cursor.execute(
        "INSERT INTO phonebook (name, phone) VALUES (%s, %s)",
        (name, phone)
    )
    connection.commit()
    print("Contact added")


# Insert from CSV
def import_csv(file_name):
    with open(file_name, 'r') as file:
        reader = csv.DictReader(file)

        for row in reader:
            cursor.execute(
                "INSERT INTO phonebook (name, phone) VALUES (%s, %s)",
                (row['name'], row['phone'])
            )

    connection.commit()
    print("CSV imported")


# Query all contacts
def show_contacts():
    cursor.execute("SELECT * FROM phonebook")
    rows = cursor.fetchall()

    for row in rows:
        print(row)


# Search by name
def search_by_name(name):
    cursor.execute(
        "SELECT * FROM phonebook WHERE name ILIKE %s",
        (f"%{name}%",)
    )

    rows = cursor.fetchall()

    for row in rows:
        print(row)


# Search by phone prefix
def search_by_prefix(prefix):
    cursor.execute(
        "SELECT * FROM phonebook WHERE phone LIKE %s",
        (f"{prefix}%",)
    )

    rows = cursor.fetchall()

    for row in rows:
        print(row)


# Update phone number
def update_phone(name, new_phone):
    cursor.execute(
        "UPDATE phonebook SET phone = %s WHERE name = %s",
        (new_phone, name)
    )

    connection.commit()
    print("Phone updated")


# Update name
def update_name(phone, new_name):
    cursor.execute(
        "UPDATE phonebook SET name = %s WHERE phone = %s",
        (new_name, phone)
    )

    connection.commit()
    print("Name updated")


# Delete by name
def delete_by_name(name):
    cursor.execute(
        "DELETE FROM phonebook WHERE name = %s",
        (name,)
    )

    connection.commit()
    print("Contact deleted")


# Delete by phone
def delete_by_phone(phone):
    cursor.execute(
        "DELETE FROM phonebook WHERE phone = %s",
        (phone,)
    )

    connection.commit()
    print("Contact deleted")

