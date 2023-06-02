"""The model file for the users"""
from pydantic import EmailStr
from database.db import Base


class User(Base):
    id: int
    email: EmailStr
    password: str