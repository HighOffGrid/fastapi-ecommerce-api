from pydantic import BaseModel, EmailStr


class UserBase(BaseModel):
     email: EmailStr

class UserCreate(UserBase):
    password: str

class UserLogin(BaseModel):
    email: EmailStr
    password: str

class UserResponse(UserBase):
    id: int
    email: EmailStr
    

    class Config:
        orm_mode = True
        