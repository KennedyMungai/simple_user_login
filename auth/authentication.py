"""The app that holds the authentication code"""
import os
from datetime import datetime, timedelta

import jwt
from dotenv import find_dotenv, load_dotenv
from fastapi import HTTPException, Security
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from passlib.context import CryptContext
