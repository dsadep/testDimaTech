from pydantic import BaseModel, EmailStr

class SUserRegData(BaseModel):
    full_name: str
    email: EmailStr
    password: str

class SUserLoginData(BaseModel):
    email: EmailStr
    password: str

class SUserMe(BaseModel):
    id: int
    email: EmailStr
    full_name: str