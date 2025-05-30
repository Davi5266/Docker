from pydantic import BaseModel

class ClientCreate(BaseModel):
    name: str
    hashed_password: str

class ClientOut(BaseModel):
    id: int
    name: str
    hashed_password: str

    class Config:
        orm_mode = True # permite que o Pydantic converta objetos do SQLAlchemy diretamente para JSON.