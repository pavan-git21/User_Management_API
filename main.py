from fastapi import FastAPI, HTTPException
import json
import os
from models import User   

app = FastAPI(title="User Management API", description="A simple API to manage users")

FILE_NAME = "users.json"

# Ensure file exists
if not os.path.exists(FILE_NAME):
    with open(FILE_NAME, "w") as f:
        json.dump([], f)

def read_users():
    with open(FILE_NAME, "r") as f:
        return json.load(f)

def write_users(data):
    with open(FILE_NAME, "w") as f:
        json.dump(data, f, indent=4)

# CREATE User
@app.post("/users")
def create_user(user: User):
    users = read_users()
    
    for u in users:
        if u["id"] == user.id:
            raise HTTPException(status_code=400, detail="User already exists")
    
    users.append(user.dict())
    write_users(users)
    return {"message": "User created successfully", "user": user}

# READ All Users
@app.get("/users")
def get_users(search: str = None, sort: str = None, order: str = "asc"):
    users = read_users()

    # --- SEARCH FILTER ---
    if search:
        search_lower = search.lower()
        users = [
            user for user in users
            if search_lower in str(user.get("name", "")).lower()
            or search_lower in str(user.get("email", "")).lower()
        ]

    #SORTING
    if sort:
        try:
            users = sorted(users, key=lambda x: x.get(sort))
        except Exception:
            raise HTTPException(status_code=400, detail="Invalid sort field")

        # DESCENDING ORDER
        if order.lower() == "desc":
            users.reverse()

    return users

# READ Single User
@app.get("/users/{user_id}")
def get_user(user_id: int):
    users = read_users()
    
    for user in users:
        if user["id"] == user_id:
            return user
    
    raise HTTPException(status_code=404, detail="User not found")

# UPDATE User
@app.put("/users/{user_id}")
def update_user(user_id: int, updated_user: User):
    users = read_users()
    
    for i, user in enumerate(users):
        if user["id"] == user_id:
            users[i] = updated_user.dict()
            write_users(users)
            return {"message": "User updated successfully"}
    
    raise HTTPException(status_code=404, detail="User not found")

# DELETE User
@app.delete("/users/{user_id}")
def delete_user(user_id: int):
    users = read_users()
    
    for user in users:
        if user["id"] == user_id:
            users.remove(user)
            write_users(users)
            return {"message": "User deleted successfully"}
    
    raise HTTPException(status_code=404, detail="User not found")