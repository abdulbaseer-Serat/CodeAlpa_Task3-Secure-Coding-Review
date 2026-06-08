import sqlite3
import bcrypt

username = "admin"
password = "123456"

hashed = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

conn = sqlite3.connect('users.db')
cursor = conn.cursor()

cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, hashed))
conn.commit()
conn.close()

print("User created!")
