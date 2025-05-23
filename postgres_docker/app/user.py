from pydantic import BaseModel
from sqlmodel import Field, Session, SQLModel, create_engine, select

class User(SQLModel, table=True):
	id: int = Field(default=None, primary_key=True)
	name: str = Field(default=None, index=True)
	email: str = Field(default=None, index=True)
	password: str = Field( default=None, index=True)
