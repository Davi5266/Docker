from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

#engine = create_engine("postgresql+psycopg2://scott:tiger@localhost:5432/mydatabase")

from sqlalchemy import URL

url_object = URL.create(
    "postgresql+psycopg2",
    username="postgres",
    password="example",  # plain (unescaped) text
    host="localhost",
    database="postgres",
)

engine = create_engine(url_object)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

from pydantic import BaseModel
from sqlmodel import Field, Session, SQLModel, create_engine, select

class User(SQLModel, table=True):
        id: int = Field(default=None, primary_key=True)
        name: str = Field(default=None, index=True)
        email: str = Field(default=None, index=True)
        password: str = Field( default=None, index=True)

Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def create_item(db,id: int,name:str, email: str, password:str):
    db_item = User(id,name,email,password)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item
    
# Usage
db = next(get_db())
new_item = create_item(db, id=0, name="Rafão", email="rafão@email.com", password="fdsfks9sd9f90ds8")
print(new_item)