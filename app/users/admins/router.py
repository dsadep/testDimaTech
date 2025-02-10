from fastapi import APIRouter, Depends, HTTPException

from app.bills.dao import BillsDAO
from app.users.admins.schemas import SUsers
from app.users.auth import get_password_hash
from app.users.dao import UsersDAO
from app.users.dependencies import get_current_user
from app.users.models import Users
from app.exceptions import AccessDeniedException, EmailAlreadyRegisteredException, UserIsNotPresentException

router = APIRouter( 
    tags=["Admins"],  
)

@router.post("/create")
async def create_user(
    full_name: str, 
    email: str, 
    password: str, 
    role: str | None = "user",
    current_user: Users = Depends(get_current_user)
):
    if current_user.role != "admin":
        raise AccessDeniedException
    existing_user = await UsersDAO.find_one_or_none(email=email)
    if existing_user:
        raise EmailAlreadyRegisteredException
    hashed_password = get_password_hash(password)
    await UsersDAO.add(full_name=full_name, email=email, role=role, hashed_password=hashed_password)

@router.delete("/delete/{user_id}")
async def delete_user(
    user_id: int,
    current_user: Users = Depends(get_current_user)
):
    if current_user.role != "admin":
        raise AccessDeniedException
    user = await UsersDAO.find_by_id(user_id)
    if not user:
        raise UserIsNotPresentException
    if current_user.id == user_id or user.role == "admin":
        raise AccessDeniedException
    await BillsDAO.delete_by_user_id(user_id)
    await UsersDAO.delete_by_id(user_id)

@router.patch("/update/{user_id}")
async def update_user(
    user_id: int, 
    role: str,
    current_user: Users = Depends(get_current_user),
):
    if current_user.role != "admin":
        raise AccessDeniedException
    user = await UsersDAO.find_by_id(user_id)
    if not user:
        raise UserIsNotPresentException
    if current_user.id == user_id or user.role == "admin":
        raise AccessDeniedException
    await UsersDAO.update_role(user_id, role)


@router.get("/users")
async def get_all_users(current_user: Users = Depends(get_current_user)) -> list[SUsers]:
    if current_user.role != "admin":
        raise AccessDeniedException
    users = await UsersDAO.find_all()
    return users