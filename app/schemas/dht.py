from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class DhtOut(BaseModel):
    id: int
    humidade: float
    temperature_c: float
    temperature_f: float
    date_time: datetime
    client_id: int

    class Config:
        orm_mode = True

class DhtBase(BaseModel):
    humidade: float
    temperature_c: float
    temperature_f: float

class DhtCreate(DhtBase):
    client_id: int  # ID do cliente a que pertence

class DhtResponse(DhtBase):
    id: int
    date_time: datetime
    client_id: int

    class Config:
        orm_mode = True
