
import psycopg2
from config import DB_CONFIG

name = input("Enter name: ")
phone = input("Enter phone: ")

conn = psycopg2.connect(**DB_CONFIG)
cur = conn.cursor()

cur.execute(
    "INSERT INTO contacts (first_name, phone) VALUES (%s, %s)",
    (name, phone)
)

conn.commit()

cur.close()
conn.close()

print("Contact added successfully!")
