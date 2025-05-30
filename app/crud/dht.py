from models.dht import Dht
from schemas.dht import DhtCreate, DhtOut
from sqlalchemy.orm import Session

# def register_dht(db: Session, dht_data: DhtCreate):
#     data_dht = Dht(**dht_data.dict())
#     db.add(data_dht)
#     db.commit()
#     db.refresh(data_dht)
#     return data_dht

# Register data dht in database
def create_dht(db: Session, dht_in: DhtCreate, id_client: int):
    dht = Dht(**dht_in.dict())
    dht.client_id = id_client
    db.add(dht)
    db.commit()
    db.refresh(dht)
    return dht

# search dht data in the database based on the id
def get_dhts_by_client(db: Session, client_id: int):
    return db.query(Dht).filter(Dht.client_id == client_id).all()

# read all dht datas
def get_all_dhts(db: Session):
    return db.query(Dht).all()
