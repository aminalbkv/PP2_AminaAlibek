
import psycopg2
from config import DB_CONFIG

print("1. Delete by name")
print("2. Delete by phone")

choice = input("Choose option: ")

conn = psycopg2.connect(**DB_CONFIG)
cur = conn.cursor()

if choice == "1":
    name = input("Enter name: ")
    cur.execute(
        "DELETE FROM contacts WHERE first_name = %s",
        (name,)
    )

elif choice == "2":
    phone = input("Enter phone: ")
    cur.execute(
        "DELETE FROM contacts WHERE phone = %s",
        (phone,)
    )

else:
    print("Invalid option!")

if choice in ("1", "2"):
    deleted = cur.rowcount
    conn.commit()
    print("Deleted contacts:", deleted)

cur.close()
conn.close()
