from pydantic import BaseModel, EmailStr, StrictStr, StrictInt
from typing import Optional


class User(BaseModel):
    username: StrictStr
    user_email: EmailStr
    user_firstname: StrictStr
    user_lastname: StrictStr

    class Config:
        orm_mode = True


class CreateUser(User):
    user_password: StrictStr


class UpdateUser(BaseModel):
    user_password: Optional[StrictStr]
    user_email: Optional[EmailStr]
    user_firstname: Optional[StrictStr]
    user_lastname: Optional[StrictStr]
