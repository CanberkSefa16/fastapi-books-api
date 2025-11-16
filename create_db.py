import sqlite3

conn = sqlite3.connect("books.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS Book(
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               title TEXT,
               author TEXT,
               page_size INTEGER
            )""")

cursor.execute("""INSERT INTO Book (title, author, page_size)
               VALUES (?, ?, ?)""",
               ("The Hobbit","J.R.R Tolkien",310))

cursor.execute("""INSERT INTO Book (title, author, page_size)
               VALUES (?, ?, ?)""",
               ("1984","George Orwell", 370))

cursor.execute("""INSERT INTO Book (title, author, page_size)
               VALUES (?, ?, ?)""",
               ("Tom Sawyer", "Mark Twain", 250))

conn.commit()
conn.close()

