from fastapi import FastAPI 
from app.users.router import router as users_router
from app.users.admins.router import router as admins_router
from app.payments.router import router as payments_router

app = FastAPI()

app.include_router(users_router)
app.include_router(admins_router)
app.include_router(payments_router)