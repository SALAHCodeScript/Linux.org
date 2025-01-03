#!/usr/bin/python3.13
import mysql.connector

host = "127.0.0.1"
port = 8000

# Establish connection
connection = mysql.connector.connect(
    host=host,
    user="root",
    password="salah",
    database="mydb"
)

# Check if the connection was successful
if connection.is_connected():
    print("Connected to MySQL Database!")

cursor = connection.cursor()
cursor.execute("SELECT employee_id, first_name FROM employees")

# Fetch all rows
rows = cursor.fetchall()

row_dict = {"IDs": [], "Names": []}
for employee_id, first_name in rows:
    row_dict["IDs"].append(employee_id)
    row_dict["Names"].append(first_name)

print(f"IDs:   {row_dict['IDs']}")
print(f"Names: {row_dict['Names']}")

# Closing the cursor
cursor.close()
