import csv
import psycopg2
import json
from pathlib import Path
from config import DB_CONFIG


def filter_by_group():
    group = input("Enter group name: ")

    with psycopg2.connect(**DB_CONFIG) as conn:
        with conn.cursor() as cur:
            cur.execute("""
                SELECT c.id, c.first_name, c.email, g.name
                FROM contacts c
                JOIN groups g ON c.group_id = g.id
                WHERE g.name ILIKE %s
                ORDER BY c.first_name
            """, (group,))

            rows = cur.fetchall()

            if not rows:
                print("No contacts found in this group.")
            else:
                for row in rows:
                    print(row)


def search_by_email():
    email = input("Enter email or part of email: ")

    with psycopg2.connect(**DB_CONFIG) as conn:
        with conn.cursor() as cur:
            cur.execute("""
                SELECT id, first_name, email
                FROM contacts
                WHERE email ILIKE %s
                ORDER BY first_name
            """, ('%' + email + '%',))

            rows = cur.fetchall()

            if not rows:
                print("No contacts found.")
            else:
                for row in rows:
                    print(row)

def sort_contacts():
    print("\nSORT CONTACTS")
    print("1. Sort by name")
    print("2. Sort by birthday")
    print("3. Sort by date added")

    choice = input("Choose sorting option: ")

    columns = {
        "1": "first_name",
        "2": "birthday",
        "3": "created_at"
    }

    if choice not in columns:
        print("Invalid option!")
        return

    column = columns[choice]

    with psycopg2.connect(**DB_CONFIG) as conn:
        with conn.cursor() as cur:
            cur.execute(f"""
                SELECT id, first_name, birthday, created_at
                FROM contacts
                ORDER BY {column} ASC NULLS LAST
            """)

            rows = cur.fetchall()

            for row in rows:
                print(row)




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
    limit = 5
    offset = 0

    while True:
        with psycopg2.connect(**DB_CONFIG) as conn:
            with conn.cursor() as cur:
                cur.execute(
                    "SELECT * FROM get_contacts_page(%s, %s)",
                    (limit, offset)
                )
                rows = cur.fetchall()

        if not rows:
            print("No contacts on this page.")
        else:
            print(f"\nPAGE {offset // limit + 1}")
            for row in rows:
                print(row)

        print("\nCommands: next / prev / quit")
        command = input("Enter command: ").lower().strip()

        if command == "next":
            if len(rows) < limit:
                print("This is the last page.")
            else:
                with psycopg2.connect(**DB_CONFIG) as conn:
                    with conn.cursor() as cur:
                        cur.execute(
                            "SELECT * FROM get_contacts_page(%s, %s)",
                            (limit, offset + limit)
                        )
                        next_rows = cur.fetchall()

                if next_rows:
                    offset += limit
                else:
                    print("This is the last page.")

        elif command == "prev":
            if offset >= limit:
                offset -= limit
            else:
                print("This is the first page.")

        elif command == "quit":
            print("Returning to main menu...")
            break

        else:
            print("Invalid command!")






def delete_contact():
    value = input("Enter name or phone to delete: ")

    with psycopg2.connect(**DB_CONFIG) as conn:
        with conn.cursor() as cur:
            cur.execute(
                "CALL delete_contact(%s)",
                (value,)
            )
    print("Delete procedure executed!")


def export_to_json():
    with psycopg2.connect(**DB_CONFIG) as conn:
        with conn.cursor() as cur:
            cur.execute("""
                SELECT
                    c.id,
                    c.first_name,
                    c.email,
                    c.birthday,
                    g.name
                FROM contacts c
                LEFT JOIN groups g ON c.group_id = g.id
                ORDER BY c.id
            """)

            contacts = []

            for row in cur.fetchall():
                contact_id, name, email, birthday, group = row

                cur.execute("""
                    SELECT phone, type
                    FROM phones
                    WHERE contact_id = %s
                    ORDER BY id
                """, (contact_id,))

                phones = []

                for phone, phone_type in cur.fetchall():
                    phones.append({
                        "phone": phone,
                        "type": phone_type
                    })

                contacts.append({
                    "name": name,
                    "email": email,
                    "birthday": birthday.isoformat() if birthday else None,
                    "group": group,
                    "phones": phones
                })

    file_path = Path(__file__).parent / "contacts.json"

    with open(file_path, "w", encoding="utf-8") as file:
        json.dump(contacts, file, indent=4, ensure_ascii=False)

    print("Contacts exported successfully!")




def import_from_json():
    file_path = Path(__file__).parent / "contacts.json"

    if not file_path.exists():
        print("JSON file not found!")
        return

    with open(file_path, "r", encoding="utf-8") as file:
        contacts = json.load(file)

    with psycopg2.connect(**DB_CONFIG) as conn:
        with conn.cursor() as cur:
            for contact in contacts:
                name = contact["name"]
                email = contact.get("email")
                birthday = contact.get("birthday")
                group = contact.get("group")
                phones = contact.get("phones", [])

                cur.execute(
                    "SELECT id FROM contacts WHERE first_name = %s",
                    (name,)
                )
                existing = cur.fetchall()

                if existing:
                    print(f"\nContact '{name}' already exists.")

                    if len(existing) > 1:
                        print("Multiple contacts have this name. Skipping.")
                        continue

                    action = input("Choose skip / overwrite: ").lower().strip()

                    if action != "overwrite":
                        print("Skipped!")
                        continue

                    contact_id = existing[0][0]

                else:
                    cur.execute(
                        "INSERT INTO contacts (first_name) VALUES (%s) RETURNING id",
                        (name,)
                    )
                    contact_id = cur.fetchone()[0]

                group_id = None

                if group:
                    cur.execute("""
                        INSERT INTO groups (name)
                        VALUES (%s)
                        ON CONFLICT (name) DO NOTHING
                    """, (group,))

                    cur.execute(
                        "SELECT id FROM groups WHERE name = %s",
                        (group,)
                    )
                    group_id = cur.fetchone()[0]

                cur.execute("""
                    UPDATE contacts
                    SET email = %s,
                        birthday = %s,
                        group_id = %s
                    WHERE id = %s
                """, (email, birthday, group_id, contact_id))

                cur.execute(
                    "DELETE FROM phones WHERE contact_id = %s",
                    (contact_id,)
                )

                for phone in phones:
                    cur.execute("""
                        INSERT INTO phones (contact_id, phone, type)
                        VALUES (%s, %s, %s)
                    """, (
                        contact_id,
                        phone["phone"],
                        phone.get("type", "mobile")
                    ))

                print(f"Imported: {name}")

    print("\nJSON import completed!")


def import_from_csv():
    file_path = Path(__file__).parent / "contacts.csv"

    if not file_path.exists():
        print("CSV file not found!")
        return

    with open(file_path, "r", encoding="utf-8-sig", newline="") as file:
        reader = csv.DictReader(file)
        contacts = list(reader)

    with psycopg2.connect(**DB_CONFIG) as conn:
        with conn.cursor() as cur:
            for contact in contacts:
                name = contact["first_name"].strip()
                phone = contact["phone"].strip()
                email = contact["email"].strip() or None
                birthday = contact["birthday"].strip() or None
                group = contact["group"].strip() or None
                phone_type = contact["phone_type"].strip().lower() or "mobile"

                if not name or not phone:
                    print("Skipped row: missing name or phone")
                    continue

                if phone_type not in ("home", "work", "mobile"):
                    print(f"Skipped {name}: invalid phone type")
                    continue

                cur.execute(
                    "SELECT id FROM contacts WHERE first_name = %s",
                    (name,)
                )

                if cur.fetchone():
                    print(f"Skipped duplicate: {name}")
                    continue

                group_id = None

                if group:
                    cur.execute("""
                        INSERT INTO groups (name)
                        VALUES (%s)
                        ON CONFLICT (name) DO NOTHING
                    """, (group,))

                    cur.execute(
                        "SELECT id FROM groups WHERE name = %s",
                        (group,)
                    )
                    group_id = cur.fetchone()[0]

                cur.execute("""
                    INSERT INTO contacts
                    (first_name, phone, email, birthday, group_id)
                    VALUES (%s, %s, %s, %s, %s)
                    RETURNING id
                """, (name, phone, email, birthday, group_id))

                contact_id = cur.fetchone()[0]

                cur.execute("""
                    INSERT INTO phones (contact_id, phone, type)
                    VALUES (%s, %s, %s)
                """, (contact_id, phone, phone_type))

                print(f"Imported: {name}")

    print("CSV import completed!")





while True:
    print("\nPHONEBOOK MENU")
    print("1. Search contacts")
    print("2. Insert or update contact")
    print("3. Bulk insert contacts")
    print("4. Show contacts with pagination")
    print("5. Delete contact")
    print("6. Filter contacts by group")
    print("7. Search contacts by email")
    print("8. Sort contacts")
    print("9. Export contacts to JSON")
    print("10. Import contacts from JSON")
    print("11. Import contacts from CSV")
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
        elif choice == "6":
            filter_by_group()
        elif choice == "7":
            search_by_email()
        elif choice == "8":
            sort_contacts()
        elif choice == "9":
            export_to_json()
        elif choice == "10":
            import_from_json()
        elif choice == "11":
            import_from_csv()
        elif choice == "0":
            print("Goodbye!")
            break
        else:
            print("Invalid option!")
    except Exception as e:
        print("Error:", e)