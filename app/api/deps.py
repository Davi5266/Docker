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

# Recebe o JWT extraido do oauth2_scheme, através de uma dependencia(Depends) que tem como parâmetro o oauth2_scheme que retorna o token extraido da requisição 
def get_current_client(token:str = Depends(oauth2_scheme),db: Session = Depends(get_db)):

    # Resposta para tratar errors de autorização de rota
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Não foi possível validar as credenciais",
        headers={"WWW-Authenticate":"Bearer"},
    )

    
    try:
        # extraindo credenciais do token
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        # pegando o parâmetro name extraido do token
        name: str = payload.get("sub")
        # Se o name não existe retorna um erro de credenciais
        if name is None:
            raise credentials_exception
    except JWTError: # Se ouver algum erro durante a extração das credenciais do token entra em uma exceção JWTError e retorna um erro de credencias
        raise credentials_exception

    # Realiza uma comparação do name extraido do token com o name do banco de dados
    client = get_name_by_client(db, name)
    # se o client for vazio retorna um erro de credenciais
    if client is None:
        raise credentials_exception
    
    return client