from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.ext.declarative import declarative_base
from pydantic import BaseModel, EmailStr, validator
from typing import Optional

Base = declarative_base()

# User model
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    role = Column(String)
    first_name = Column(String, nullable=True)
    last_name = Column(String, nullable=True)
    date_of_birth = Column(Date, nullable=True)
    designation = Column(String, nullable=True)

# Pydantic models
class UserCreate(BaseModel):
    email: EmailStr
    password: str
    role: str
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    date_of_birth: Optional[str] = None  # Expecting 'YYYY-MM-DD' format
    designation: Optional[str] = None

class UserLogin(BaseModel):
    email: EmailStr
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str

class UserUpdate(BaseModel):
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    date_of_birth: Optional[str] = None
    designation: Optional[str] = None

class UserResponse(BaseModel):
    email: EmailStr
    role: str
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    date_of_birth: Optional[str] = None
    designation: Optional[str] = None

    @validator('date_of_birth', pre=True, always=True)
    def format_date_of_birth(cls, v):
        return v.strftime('%Y-%m-%d') if v else None

    class Config:
        orm_mode = True
