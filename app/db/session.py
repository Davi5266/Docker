from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DATABASE_URL = f'postgresql+psycopg2://datauser:123456789@127.0.0.1:5432/meubanco'

engine = create_engine(DATABASE_URL)
# SessionLocal = sessionmaker(engine)  
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()