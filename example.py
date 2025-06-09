from mysql_helper import MySqlHelper

db = MySqlHelper(
    host="localhost",
    user="root",
    password="your_password",
    database="student_db"
)

# Select
print(db.query("SELECT * FROM student"))

# Insert
db.execute("INSERT INTO student (name, height) VALUES (%s, %s)", ("Alice", 1.65))

# Insert many
db.executemany(
    "INSERT INTO student (name, height) VALUES (%s, %s)",
    [("Bob", 1.78), ("Charlie", 1.80)]
)

db.close()

