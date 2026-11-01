
import psycopg2
from config import DB_CONFIG

print("1. Search by name")
print("2. Search by phone prefix")

choice = input("Choose option: ")

conn = psycopg2.connect(**DB_CONFIG)
cur = conn.cursor()

if choice == "1":
    name = input("Enter name: ")

    cur.execute(
        "SELECT * FROM contacts WHERE first_name ILIKE %s",
        ("%" + name + "%",)
    )

elif choice == "2":
    prefix = input("Enter phone prefix: ")

    cur.execute(
        "SELECT * FROM contacts WHERE phone LIKE %s",
        (prefix + "%",)
    )

else:
    print("Invalid option!")
    cur.close()
    conn.close()
    exit()

results = cur.fetchall()

for contact in results:
    print(contact)

if not results:
    print("No contacts found.")

cur.close()
conn.close()
