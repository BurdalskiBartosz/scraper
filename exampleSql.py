import sqlite3

connection = sqlite3.connect("data.db")
cursor = connection.cursor()

cursor.execute("SELECT * FROM events WHERE date='2018.10.15'")
rows = cursor.fetchall()

print(rows)


cursor.execute("SELECT band, date FROM events WHERE date='2018.10.15'")
rows = cursor.fetchall()

print(rows)


new_rows = [('Dog', 'Dog city', '2020.11.15'),
            ('Horse', 'Horse city', '2020.11.15')]

cursor.executemany("INSERT INTO events VALUES(?,?,?)", new_rows)
connection.commit()

cursor.execute("SELECT * FROM events ")
rows = cursor.fetchall()

print(rows)
