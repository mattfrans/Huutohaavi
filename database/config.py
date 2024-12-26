from dotenv import load_dotenv
import os

load_dotenv()

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'postgresql://postgres:postgres@localhost/uusimaa_real_estate')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
