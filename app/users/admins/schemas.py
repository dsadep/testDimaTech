from pydantic import BaseModel

class SUsers(BaseModel):
    id: int
    full_name: str
    email: str
    role: str