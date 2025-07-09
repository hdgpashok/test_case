import sqlite3

connection = sqlite3.connect('reviews.db')
cursor = connection.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS reviews (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  text TEXT NOT NULL,
  sentiment TEXT NOT NULL,
  created_at TEXT NOT NULL
)
''')
