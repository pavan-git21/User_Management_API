*User Management API*


A simple RESTful API built with FastAPI to manage users. Supports full CRUD operations with search and sorting capabilities. User data is persisted in a local JSON file.

*Tech Stack*

FastAPI – Web framework

Pydantic – Data validation via models

Uvicorn – ASGI server

JSON file – Lightweight local storage (users.json)


*Project Structure*

 main.py          # API routes and business logic
 
 models.py        # Pydantic User model
 
 users.json       # Auto-generated data store
 
 requirements.txt # Dependencies


1. Install Dependencies
pip install fastapi uvicorn pydantic
2. Run the Server

uvicorn main:app --reload
The API will be available at http://127.0.0.1:8000/docs
