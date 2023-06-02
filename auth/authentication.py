"""The app that holds the authentication code"""
import os
from datetime import datetime, timedelta

import jwt
from dotenv import find_dotenv, load_dotenv
from fastapi import HTTPException, Security, status
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from passlib.context import CryptContext

load_dotenv(find_dotenv())

SECRET_KEY = os.environ.get("SECRET_KEY")


class AuthHandler():
    """The class that handles authentication for the app"""
    security = HTTPBearer()
    pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
    
    def get_password_hash(self, password: str):
        """The function that hashes the password

        Args:
            password (Str): The password in plain text

        Returns:
            hashed_password: The password hash
        """
        return self.pwd_context.hash(password)

    def verify_password(self, plain_password: str, hashed_password: str):
        """The function to verify the password based on its hash

        Args:
            plain_password (str): The password in plain text
            hashed_password (str): The hash of the password

        Returns:
            bool: Whether the password and its hash match
        """
        return self.pwd_context.verify(plain_password, hashed_password)
    
    def encode_token(self, user_id: int):
        """The function to encode the token for the user

        Args:
            user_id (The id of the user): The user id

        Returns:
           str: The jwt
        """
        payload = {
            'exp': datetime.utcnow() + timedelta(days=0, minutes=5),
            'iat': datetime.utcnow(),
            'sub': user_id
        }
        
        return jwt.encode(payload, SECRET_KEY, algorithm='HS256')
    
    def decode_token(self, token: str):
        """A function to decode the token

        Args:
            token (str): The token to be decoded

        Raises:
            HTTPException: A 401 is raised if the token has expired
            HTTPException: A 401 is raised if the token is invalid

        Returns:
           str: A string of the user id
        """
        try:
          payload = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
          return payload['sub']
        except jwt.ExpiredSignatureError:
          raise HTTPException(
              status_code=status.HTTP_401_UNAUTHORIZED, 
              detail="The signature has expired"
              )
        except jwt.InvalidTokenError:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED, 
                detail="Invalid token"
                )