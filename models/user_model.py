"""The model file for the users"""
from pydantic import EmailStr

from database.db import Base


class User(Base):
    """The model for the User data

    Args:
        Base (Declarative Base): The basis for the models
    """
    __tablename__ = "users"
    
    id: int
    email: EmailStr
    password: str