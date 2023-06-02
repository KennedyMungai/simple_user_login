"""The users schema file"""
from pydantic import BaseModel, EmailStr


class UserBase(BaseModel):
    """The base for the User schemas

    Args:
        BaseModel (Pydantic): _description_
    """
    email: EmailStr
    
class UserCreate(UserBase):
    """The schema for creating a user

    Args:
        UserBase (Pydantic): The base for creating schemas
    """
    password: str
    
    
class User(UserBase):
    """The schema for the user data

    Args:
        UserBase (Pydantic): The base schema for the user data
    """
    id: int
    
    class Config:
        """The config for the user schema"""
        orm_mode = True