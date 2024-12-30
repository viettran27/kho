import os
from dotenv import load_dotenv
from sqlalchemy.engine import URL

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../'))
load_dotenv(os.path.join(BASE_DIR, '.env'))

class Settings():
    SECRET_KEY = os.getenv('SECRET_KEY', '')
    API_PREFIX = ''
    BACKEND_CORS_ORIGINS = ['*']
    DATABASE_URL = URL.create(
        "mssql+pyodbc",
        username=os.getenv("USERNAME_DB"),
        password=os.getenv("PASSWORD_DB"),
        host=os.getenv("HOST"),
        database=os.getenv("DATABASE"),
        query={
           "driver": "ODBC Driver 17 for SQL Server",
           "TrustServerCertificate": "yes" 
        }
    )

settings = Settings()