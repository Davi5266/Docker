from fastapi import FastAPI
from api.routes import dht, client

# Config DB
from db.base import Base
from db import base_model_imports
from db.session import engine
# create all tables
Base.metadata.create_all(bind=engine)

app = FastAPI()
# Routes
app.include_router(dht.router)
app.include_router(client.router)


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(
        "main:app",
        port=8000,
        host="0.0.0.0",
        log_level="info",
        reload=True)
