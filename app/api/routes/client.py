from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordRequestForm

from crud.client import register_client, all_clients, get_name_by_client
from api.deps import get_db, get_current_client
from schemas.client import ClientCreate, ClientOut
from schemas.token import Token
from core.security import verify_password, create_access_token

router = APIRouter(prefix="/client", tags=["client"])

@router.post("/register")
def client_register(data:ClientCreate, db: Session = Depends(get_db)):
    # try:
    #     return register_client(db, data)

    # except Exception as e:
    #     print(e)
    #     return {"Erro": e}
    print(data)
    return register_client(db, data)
@router.get("/all",  response_model=list[ClientOut])
def viwer_all_clients(db: Session = Depends(get_db)):
    return all_clients(db)

@router.post("/login", response_model=Token)
def login_client(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    client = get_name_by_client(db,form_data.username)
    if not client or not verify_password(form_data.password, client.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Credenciais inválidas"
        )
    try:
        access_token = create_access_token(data={"sub":client.name})
        return {"access_token":access_token, "token_type":"bearer"}
    except Exception:
        return {"erro":"falha nas credencias","type error":Exception}

@router.get("/me")
def read_logged_client(current_client: ClientOut = Depends(get_current_client)):
    return {
        "id": current_client.id,
        "name": current_client.name
    }