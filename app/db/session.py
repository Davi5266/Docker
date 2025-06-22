from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

import socket

import os

hostname = socket.gethostname()
IPAddr = socket.gethostbyname(hostname)

POSTGRES_USER = os.getenv("POSTGRES_USER")
POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD")
POSTGRES_DB = os.getenv("POSTGRES_DB")

DATABASE_URL = f'postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@db:5432/{POSTGRES_DB}'
#DATABASE_URL = f'postgresql://teste2025:1234567890@db:5432/meudb2025'

print(DATABASE_URL)

# DATABASE_URL = f'postgresql+psycopg2://datauser:123456789@127.0.0.1:5432/meubanco'
#DATABASE_URL = f'postgresql+psycopg2://datauser:123456789@{IPAddr}:5432/meubanco'

#DATABASE_URL = os.getenv("DATABASE_URL")
engine = create_engine(DATABASE_URL)

#print("IP LOCAL" + IPAddr)

#engine = create_engine(DATABASE_URL)
# SessionLocal = sessionmaker(engine)  
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
