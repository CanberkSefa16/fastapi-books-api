FastAPI Books API
------------------------------------------------
A simple CRUD API built with FastAPI and SQLite.
This project demonstrates basic backend development concepts such as routing, database operations, Pydantic models, and RESTful design.


Features
-------------------------------------
-Create, read, update, delete books

-SQLite database

-Pydantic request/response models

-Automatic API documentation via Swagger


1 Run the API --> "uvicorn main:app --reload"
2 Open in browser --> "http://localhost:8000/docs"



Endpoints
---------------------------
GET /books — List all books

POST /books — Create a new book

PUT /books/{id} — Update a book

DELETE /books/{id} — Delete a book

GET /health — Health check

GET /books{id} — Get book by id



Requirements
------------
-fastapi
-uvicorn