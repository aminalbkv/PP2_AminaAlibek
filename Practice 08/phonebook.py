
import psycopg2
from config import DB_CONFIG


def search_contacts():
    pattern = input("Enter name or phone: ")

    with psycopg2.connect(**DB_CONFIG) as conn:
        with conn.cursor() as cur:
            cur.execute(
                "SELECT * FROM search_contacts(%s)",
                (pattern,)
            )
            for row in cur.fetchall():
                print(row)


def upsert_contact():
    name = input("Enter name: ")
    phone = input("Enter phone: ")

    with psycopg2.connect(**DB_CONFIG) as conn:
        with conn.cursor() as cur:
            cur.execute(
                "CALL upsert_contact(%s, %s)",
                (name, phone)
            )
    print("Contact added or updated!")


def bulk_insert():
    names = ["AliTest", "DanaTest", "WrongTest"]
    phones = ["87071112233", "77074445566", "123"]

    with psycopg2.connect(**DB_CONFIG) as conn:
        with conn.cursor() as cur:
            cur.execute(
                "CALL bulk_insert_contacts(%s::text[], %s::text[], NULL)",
                (names, phones)
            )
            print("Invalid data:", cur.fetchone()[0])


def pagination():
    limit = int(input("Enter limit: "))
    offset = int(input("Enter offset: "))

    with psycopg2.connect(**DB_CONFIG) as conn:
        with conn.cursor() as cur:
            cur.execute(
                "SELECT * FROM get_contacts_page(%s, %s)",
                (limit, offset)
            )
            for row in cur.fetchall():
                print(row)


def delete_contact():
    value = input("Enter name or phone to delete: ")

    with psycopg2.connect(**DB_CONFIG) as conn:
        with conn.cursor() as cur:
            cur.execute(
                "CALL delete_contact(%s)",
                (value,)
            )
    print("Delete procedure executed!")


while True:
    print("\nPHONEBOOK MENU")
    print("1. Search contacts")
    print("2. Insert or update contact")
    print("3. Bulk insert contacts")
    print("4. Show contacts with pagination")
    print("5. Delete contact")
    print("0. Exit")

    choice = input("Choose option: ")

    try:
        if choice == "1":
            search_contacts()
        elif choice == "2":
            upsert_contact()
        elif choice == "3":
            bulk_insert()
        elif choice == "4":
            pagination()
        elif choice == "5":
            delete_contact()
        elif choice == "0":
            print("Goodbye!")
            break
        else:
            print("Invalid option!")
    except Exception as e:
        print("Error:", e)
