from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from typing import List

from crud.dht import *
from api.deps import get_db
from schemas.dht import DhtCreate, DhtOut, DhtResponse
from schemas.token import Token
from schemas.client import ClientOut
from api.deps import get_current_client

# router = APIRouter(prefix="/dht", tags=["dht"])
# Criando um rota privada
router = APIRouter(
    prefix="/dht",
    tags=["DHT"],
    dependencies=[Depends(get_current_client)]
    )

# @router.post("/register",response_model=DhtResponse)
# def register_data(data:DhtCreate ,db: Session = Depends(get_db)):
#     return register_dht(db, data)

# register data dht
# @router.post("/", response_model=DhtResponse)
# def create_dht_record(dht_in: DhtCreate, db: Session = Depends(get_db)):
#     return create_dht(db, dht_in)

@router.post("/securitycreate", response_model=DhtResponse)
def security_create_dht_record(dht_in: DhtCreate, db: Session = Depends(get_db), current_client: ClientOut = Depends(get_current_client)):
    id = current_client.id
    return create_dht(db, dht_in, int(id))


# search for dht data by the client's ip 
@router.get("/client/{client_id}", response_model=List[DhtResponse])
def get_client_dht_data(client_id: int, db: Session = Depends(get_db)):
    return get_dhts_by_client(db, client_id)

# read all data dht 
@router.get("/", response_model=List[DhtResponse])
def get_all_dht_data(db: Session = Depends(get_db)):
    return get_all_dhts(db)
