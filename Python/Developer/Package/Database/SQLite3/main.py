import sqlite3

conn = sqlite3.connect('data.db')

c = conn.cursor()

c.execute("""CREATE TABLE IF NOT EXISTS custom(
    name TEXT,
    age INT
);""")

c.execute("""INSERT INTO custom
VALUES ('Salah', 20);""")

print(c.execute("SELECT * FROM custom").fetchall())
