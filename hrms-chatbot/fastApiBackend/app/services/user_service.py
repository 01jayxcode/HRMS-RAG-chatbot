from app.db.json_db import read_data, write_data
from app.utils.time_utils import get_current_time

def create_user(user):
    data = read_data()
    data.append(user.dict())
    write_data(data)
    return user

def get_users():
    return read_data()

def get_user(user_id: int):
    data = read_data()
    for user in data:
        if user["id"] == user_id:
            return user
    return {"error": "User not found"}

def delete_user(user_id: int):
    data = read_data()
    new_data = [u for u in data if u["id"] != user_id]
    write_data(new_data)
    return {"message": "Deleted"}

def add_message(user_id: int, message: str):
    data = read_data()

    for user in data:
        if user["id"] == user_id:
            user["messages"].append({
                "message": message,
                "timestamp":  get_current_time().isoformat()
            })
            write_data(data)
            return user

    return {"error": "User not found"}