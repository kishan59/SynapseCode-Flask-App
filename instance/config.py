import os

# Flask Configuration - uses environment variable for SECRET_KEY from .env
SECRET_KEY = os.environ.get('SECRET_KEY')

# SQLAlchemy Configuration (for SQLite development database)
SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///synapsecode.db'
SQLALCHEMY_TRACK_MODIFICATIONS = False # Suppress SQLAlchemy track modifications warning