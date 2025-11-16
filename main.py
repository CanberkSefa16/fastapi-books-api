from fastapi import FastAPI, HTTPException
import sqlite3
from pydantic import BaseModel

class BookCreate(BaseModel):
    title: str
    author: str
    page_size: int
class BookOut(BaseModel):
    id: int
    title: str
    author: str
    page_size: int

app = FastAPI()

@app.get("/health")
def health():
    return {"message": "API is working!"}

@app.get("/books", response_model=list[BookOut])
def get_all_books():
    
    conn = sqlite3.connect("books.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM Book")
    records = cursor.fetchall()

    books = []
    
    for record in records:
        book = {
            "id": record[0],
            "title": record[1],
            "author": record[2],
            "page_size": record[3]
        }
        books.append(book)
    conn.close()

    return books

@app.post("/books", response_model=BookOut)
def create_book(book: BookCreate):
    
    conn = sqlite3.connect("books.db")
    cursor = conn.cursor()

    cursor.execute("INSERT INTO Book (title, author, page_size) VALUES (?, ?, ?)",(book.title, book.author, book.page_size))
    conn.commit()
    new_id = cursor.lastrowid
    conn.close()

    return {
        "id": new_id,
        "title": book.title,
        "author": book.author,
        "page_size": book.page_size
    }

@app.delete("/books/{id}")
def delete_book(id: int):

    conn = sqlite3.connect("books.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM Book WHERE id=?",(id,))
    book = cursor.fetchone()

    if book is None:
        conn.close()
        raise HTTPException(status_code=404, detail="Book not found!")
    cursor.execute("DELETE FROM Book WHERE id=?", (id,))
    conn.commit()
    conn.close()

    return {
        "message": "Book deleted!",
        "book": {
            "id": id,
            "title": book[1],
            "author": book[2],
            "page_size": book[3]
        }
    }

@app.put("/books/{id}", response_model=BookOut)
def update_book(id: int, book: BookCreate):

    conn = sqlite3.connect("books.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM Book WHERE id=?", (id,))
    record = cursor.fetchone()

    if record is None:
        conn.close()
        raise HTTPException(status_code=404, detail="Book not found!")
    
    cursor.execute("UPDATE Book SET title=?, author=?, page_size=? WHERE id=?", (book.title, book.author, book.page_size, id))
    conn.commit()
    conn.close()

    return {
        "id": id,
        "title": book.title,
        "author": book.author,
        "page_size": book.page_size
    }
