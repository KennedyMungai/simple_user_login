"""The app that holds the authentication code"""
from datetime import datetime, timedelta

import jwt
from fastapi import HTTPException, Security
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from passlib.context import CryptContext
