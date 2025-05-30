from passlib.context import CryptContext
from jose import JWTError, jwt
from datetime import datetime, timedelta
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from api.deps import get_db

# config bcrypt
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Recebe uma senha digitada pelo usuário e a criptografa
def hash_password(password:str) -> str:
    return pwd_context.hash(password)

# Realiza uma comparação entre a senha digitada com a senha registrada no sistema
def verify_password(plain_password:str, hashed_password:str) -> bool:
    # A senha digitada é criptografada e o seu hash é comparado com o hash no sistema
    return pwd_context.verify(plain_password, hashed_password)

# config JWT
SECRET_KEY = "" # signature token
ALGORITHM = "HS256" # hash type
ACCESS_TOKEN_EXPIRE_MINUTES = 30 # Validation token

# a função create_access_token gera um token com base em dois parêmtros, data que armazena infomações do usuário, e o expires_delta que define um tempo de expiração opcional
def create_access_token(data:dict, expires_delta:timedelta | None = None):

    to_encode = data.copy() # cópia dos dados gerados pelo usuário
    expire = datetime.utcnow() + (expires_delta or timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)) # Define o tempo de vida do JWT, se o expires_delta for None(vazio) o tempo padrão vai ser de 15 minutos 

    to_encode.update({"exp":expire}) # passa o tempo de expiração do JWT como parâmetro do dicionario data
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM) # codifica o token JWT com algoritmo HS256 e uma chave secreta
    return encoded_jwt

# Verificador de token
def verify_token(token:str):
    # Recebe o token do usuário como parâmetro, e tenta decodificar caso de error a função entra na exceção JWTError e retorna vazio(None)
    try:
        # Decodificando o token atribuido e utilizando como parâmetro a chave secreta(SECRET_KEY) e o algoritmo(ALGORITHM)
        payload = jwt.decode(token, SECRET_KEY, algorithms=ALGORITHM)
        return payload
    except JWTError:
        return None
    
# Dependencia que extrai o token JWT do cabeçalho {Authorization: Bearer <token>}, e o parâmetro tokenUrl passa o endpoint reponsavel por fornecer o token, através de uma rota POST /login que passa um body com username e password (no caso desse código ele passa um body com email e password)
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="client/login")
