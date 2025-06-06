from sqlalchemy import Column, String, Float, ForeignKey, Integer, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from db.base import Base

class Dht(Base):
    __tablename__ = "dht"

    id = Column(Integer, primary_key=True, index=True)
    humidity = Column(Float, index=True)
    temperature_c = Column(Float, index=True)
    temperature_f = Column(Float, index=True)
    date_time = Column(DateTime, default=datetime.utcnow)

    client_id = Column(Integer, ForeignKey("client.id"))
    client = relationship("Client", back_populates="dht")