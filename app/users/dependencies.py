from datetime import datetime
from fastapi import Depends, HTTPException, Request
from jose import jwt, JWTError
from app.config import settings
from app.exceptions import UserIsNotAuntificatedException, InvalidTokenException, TokenExpiredException, UserIsNotPresentException
from app.users.dao import UsersDAO

def get_token(request: Request):
    token = request.cookies.get("user_access_token")
    if token is None:
        raise UserIsNotAuntificatedException
    return token

async def get_current_user(token: str = Depends(get_token)):
    try:
        payload = jwt.decode(
            token, settings.SECRET_KEY, algorithms=settings.ALGORITHM
        )
    except JWTError:
        raise InvalidTokenException

    expire: str = payload.get("exp")
    if (not expire) or (int(expire) < datetime.now().timestamp()): 
        raise TokenExpiredException
    
    user_id: str = payload.get("sub")
    if not user_id:
        raise UserIsNotPresentException
    
    user = await UsersDAO.find_by_id(int(user_id))
    if not user:
        raise UserIsNotPresentException
    
    return user