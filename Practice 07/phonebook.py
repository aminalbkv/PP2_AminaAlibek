
import csv
import psycopg2
from pathlib import Path
from config import DB_CONFIG


def add_contact():
    name = input("Enter name: ")
    phone = input("Enter phone: ")

    with psycopg2.connect(**DB_CONFIG) as conn:
        with conn.cursor() as cur:
            cur.execute(
                "INSERT INTO contacts (first_name, phone) VALUES (%s, %s)",
                (name, phone)
            )

    print("Contact added!")


def show_contacts():
    with psycopg2.connect(**DB_CONFIG) as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM contacts ORDER BY id")
            for contact in cur.fetchall():
                print(contact)


def search_contact():
    print("1. Search by name")
    print("2. Search by phone prefix")
    choice = input("Choose: ")

    if choice == "1":
        name = input("Enter name: ")
        query = "SELECT * FROM contacts WHERE first_name ILIKE %s"
        value = ("%" + name + "%",)

    elif choice == "2":
        prefix = input("Enter phone prefix: ")
        query = "SELECT * FROM contacts WHERE phone LIKE %s"
        value = (prefix + "%",)

    else:
        print("Invalid option!")
        return

    with psycopg2.connect(**DB_CONFIG) as conn:
        with conn.cursor() as cur:
            cur.execute(query, value)
            results = cur.fetchall()

    if results:
        for contact in results:
            print(contact)
    else:
        print("No contacts found.")


def update_contact():
    print("1. Update phone")
    print("2. Update name")
    choice = input("Choose: ")

    if choice == "1":
        name = input("Enter name: ")
        phone = input("Enter new phone: ")
        query = "UPDATE contacts SET phone = %s WHERE first_name = %s"
        values = (phone, name)

    elif choice == "2":
        old_name = input("Enter old name: ")
        new_name = input("Enter new name: ")
        query = "UPDATE contacts SET first_name = %s WHERE first_name = %s"
        values = (new_name, old_name)

    else:
        print("Invalid option!")
        return

    with psycopg2.connect(**DB_CONFIG) as conn:
        with conn.cursor() as cur:
            cur.execute(query, values)
            print("Updated contacts:", cur.rowcount)


def delete_contact():
    print("1. Delete by name")
    print("2. Delete by phone")
    choice = input("Choose: ")

    if choice == "1":
        name = input("Enter name: ")
        query = "DELETE FROM contacts WHERE first_name = %s"
        value = (name,)

    elif choice == "2":
        phone = input("Enter phone: ")
        query = "DELETE FROM contacts WHERE phone = %s"
        value = (phone,)

    else:
        print("Invalid option!")
        return

    with psycopg2.connect(**DB_CONFIG) as conn:
        with conn.cursor() as cur:
            cur.execute(query, value)
            print("Deleted contacts:", cur.rowcount)



def import_csv():
    path = Path(__file__).parent / "contacts.csv"
    added = 0

    with open(path, "r") as file:
        reader = csv.DictReader(file)

        with psycopg2.connect(**DB_CONFIG) as conn:
            with conn.cursor() as cur:
                for row in reader:
                    cur.execute(
                        "SELECT 1 FROM contacts WHERE first_name = %s AND phone = %s",
                        (row["first_name"], row["phone"])
                    )

                    if cur.fetchone() is None:
                        cur.execute(
                            "INSERT INTO contacts (first_name, phone) VALUES (%s, %s)",
                            (row["first_name"], row["phone"])
                        )
                        added += 1

    print("New contacts imported:", added)


while True:
    print("\n===== PHONEBOOK =====")
    print("1. Add contact")
    print("2. Show all contacts")
    print("3. Search contact")
    print("4. Update contact")
    print("5. Delete contact")
    print("6. Import CSV")
    print("0. Exit")

    choice = input("Choose option: ")

    if choice == "1":
        add_contact()
    elif choice == "2":
        show_contacts()
    elif choice == "3":
        search_contact()
    elif choice == "4":
        update_contact()
    elif choice == "5":
        delete_contact()
    elif choice == "6":
        import_csv()
    elif choice == "0":
        print("Goodbye!")
        break
    else:
        print("Invalid option!")

