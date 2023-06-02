"""The db connection file"""
import os

from dotenv import find_dotenv, load_dotenv
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


load_dotenv(find_dotenv())