"""The app that holds the authentication code"""
import os
from datetime import datetime, timedelta

import jwt
from dotenv import find_dotenv, load_dotenv
from fastapi import HTTPException, Security
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from passlib.context import CryptContext


load_dotenv(find_dotenv())

SECRET_KEY = os.environ.get("SECRET_KEY")


class AuthHandler():
    """The class that handles authentication for the app"""
    security = HTTPBearer()
    pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
    
    def get_password_hash(self, password):
        return self.pwd_context.hash(password)

    def verify_password(self, plain_password, hashed_password):
        return self.pwd_context.verify(plain_password, hashed_password)