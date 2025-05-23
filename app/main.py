from fastapi import FastAPI
import mysql.connector
import os

app = FastAPI()

@app.get("/")
def home():
    return {"mensagem": "API funcionando com MySQL!"}

@app.get("/db")
def testar_conexao():
    try:
        conn = mysql.connector.connect(
            host=os.getenv("DB_HOST"),
            user=os.getenv("MYSQL_USER"),
            password=os.getenv("MYSQL_PASSWORD"),
            database=os.getenv("MYSQL_DATABASE")
        )
        conn.close()
        return {"mensagem": "Conexão com MySQL OK!"}
    except Exception as e:
        return {"erro": str(e)}

