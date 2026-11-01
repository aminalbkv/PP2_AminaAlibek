
import psycopg2
from config import DB_CONFIG

print("1. Update phone")
print("2. Update name")

choice = input("Choose option: ")

conn = psycopg2.connect(**DB_CONFIG)
cur = conn.cursor()

if choice == "1":
    name = input("Enter name: ")
    new_phone = input("Enter new phone: ")

    cur.execute(
        "UPDATE contacts SET phone = %s WHERE first_name = %s",
        (new_phone, name)
    )

elif choice == "2":
    old_name = input("Enter old name: ")
    new_name = input("Enter new name: ")

    cur.execute(
        "UPDATE contacts SET first_name = %s WHERE first_name = %s",
        (new_name, old_name)
    )

else:
    print("Invalid option!")

conn.commit()

if choice in ("1", "2"):
    print("Updated contacts:", cur.rowcount)

cur.close()
conn.close()
