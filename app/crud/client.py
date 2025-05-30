from models.client  import Client
from schemas.client import ClientCreate, ClientOut
from sqlalchemy.orm import Session
from core.security import hash_password

def register_client(db:Session, client_data: ClientCreate):
    hashed_password = hash_password(client_data.hashed_password)
    data_client = Client(name=client_data.name, hashed_password = hashed_password)
    db.add(data_client)
    db.commit()
    db.refresh(data_client)
    return data_client

def all_clients(db:Session):
    return  db.query(Client).all()

def get_name_by_client(db: Session, name: str):
    return db.query(Client).filter(Client.name == name).first()