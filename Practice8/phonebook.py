from connect import get_connection


def call_search(pattern):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("SELECT * FROM search_contacts(%s);", (pattern,))
    rows = cur.fetchall()

    for row in rows:
        print(row)

    conn.close()


def call_pagination(limit, offset):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("SELECT * FROM get_contacts_paginated(%s, %s);", (limit, offset))
    rows = cur.fetchall()

    for row in rows:
        print(row)

    conn.close()


def upsert(name, phone):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("CALL upsert_contact(%s, %s);", (name, phone))
    conn.commit()

    conn.close()


def insert_many():
    conn = get_connection()
    cur = conn.cursor()

    names = ['Alice', 'Bob', 'Charlie']
    phones = ['1234567890', 'invalid123', '9876543210']

    cur.execute("CALL insert_many_contacts(%s, %s);", (names, phones))
    conn.commit()

    conn.close()


def delete(value):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("CALL delete_contact(%s);", (value,))
    conn.commit()

    conn.close()


if __name__ == "__main__":
    print("1 - Search")
    print("2 - Pagination")
    print("3 - Upsert")
    print("4 - Bulk insert")
    print("5 - Delete")

    choice = input("Choose: ")

    if choice == "1":
        call_search(input("Pattern: "))

    elif choice == "2":
        call_pagination(int(input("Limit: ")), int(input("Offset: ")))

    elif choice == "3":
        upsert(input("Name: "), input("Phone: "))

    elif choice == "4":
        insert_many()

    elif choice == "5":
        delete(input("Name or Phone: "))