from fastapi import APIRouter
from app.models.user import User
from app.services.user_service import (
    create_user,
    get_users,
    get_user,
    delete_user,
    add_message
)

router = APIRouter()

@router.post("/user")
def create(user: User):
    return create_user(user)

@router.get("/users")
def get_all():
    return get_users()

@router.get("/users/{user_id}")
def get_one(user_id: int):
    return get_user(user_id)

@router.delete("/users/{user_id}")
def delete(user_id: int):
    return delete_user(user_id)

@router.post("/users/{user_id}/message")
def send_message(user_id: int, message: str):
    return add_message(user_id, message)