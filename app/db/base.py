# app/db/base.py

from sqlalchemy.ext.declarative import as_declarative, declared_attr

@as_declarative()
class Base:
    # id: any
    __name__: str

    # Garante que todas as tabelas tenham um nome padrão baseado no nome da classe
    @declared_attr
    def __tablename__(cls) -> str:
        return cls.__name__.lower()
