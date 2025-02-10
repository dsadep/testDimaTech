from fastapi import APIRouter, Depends, HTTPException, Response

from app.bills.dao import BillsDAO
from app.exceptions import AlreadyLoggedInException, BillNotFoundException, TransactionsNotFoundException
from app.exceptions import InvalidPasswordOrEmailException, EmailAlreadyRegisteredException
from app.payments.dao import TransactionsDAO
from app.users.auth import authenticate_user, create_access_token, get_password_hash
from app.users.dao import UsersDAO
from app.users.dependencies import get_current_user
from app.users.models import Users
from app.users.schemas import SUserRegData, SUserLoginData, SUserMe
from app.bills.schemas import SUserBill
from app.payments.schemas import SUserTransactions


router = APIRouter(
    prefix="/users",
    tags=["Auth, Users"]
)

@router.post("/register")
async def register_user(
    user_data : SUserRegData
) -> SUserMe:
    existing_user = await UsersDAO.find_one_or_none(email=user_data.email)
    if existing_user:
        raise EmailAlreadyRegisteredException
    hashed_password = get_password_hash(user_data.password)
    new_user = await UsersDAO.add(full_name=user_data.full_name, email=user_data.email, role="user", hashed_password=hashed_password)
    await BillsDAO.add(user_id=new_user.id, balance=0.0)
    return new_user
    

@router.post("/login")
async def login_user(
    response: Response, 
    user_data: SUserLoginData
):
    user = await authenticate_user(user_data.email, user_data.password)
    if not user:
        raise InvalidPasswordOrEmailException
    access_token = create_access_token({"sub" : str(user.id)})
    response.set_cookie("user_access_token", access_token, httponly=True)
    return access_token 

@router.post("/logout")
async def logout_user(response: Response):
    response.delete_cookie("user_access_token")

@router.get("/me")
async def get_user_info(current_user: Users = Depends(get_current_user)) -> SUserMe:
    return current_user

@router.get("/balance")
async def get_user_balances(current_user: Users = Depends(get_current_user)) -> list[SUserBill]:
    bill = await BillsDAO.find_all(user_id=current_user.id)
    if not bill:
        raise BillNotFoundException
    return bill

@router.get("/transactions")
async def get_user_transactions(current_user: Users = Depends(get_current_user)) -> list[SUserTransactions]:
    transactions = await TransactionsDAO.find_all(user_id=current_user.id)
    if not transactions:
        raise TransactionsNotFoundException
    return transactions