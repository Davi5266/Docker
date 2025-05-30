from db.session import get_db
from core.security import oauth2_scheme
from sqlalchemy.orm import Session
from fastapi import Depends, HTTPException,status
from jose import JWTError,jwt

from crud.client import get_name_by_client
from core.security import SECRET_KEY, ALGORITHM

# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()


def get_current_client(token:str = Depends(oauth2_scheme),db: Session = Depends(get_db)):

    # Resposta para tratar errors de autorização de rota
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Não foi possível validar as credenciais",
        headers={"WWW-Authenticate":"Bearer"},
    )

    
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        
        name: str = payload.get("sub")
        
        if name is None:
            raise credentials_exception
    except JWTError: 
        raise credentials_exception

    client = get_name_by_client(db, name)
    
    if client is None:
        raise credentials_exception
    
    return client