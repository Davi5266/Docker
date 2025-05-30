from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import relationship
from db.base import Base

class Client(Base):
    __tablename__="client"
    id = Column(Integer, primary_key=True,autoincrement=True, index=True)
    name = Column(String(50),unique = True, index=True)
    hashed_password = Column(String(255), index=True)

    dht = relationship("Dht", back_populates="client")