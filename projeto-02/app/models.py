from sqlalchemy import Column, Integer, String, Float, DateTime
from sqlalchemy.orm import declarative_base
from datetime import datetime

BRT = timezone(timedelta(hours=-3))

Base = declarative_base()

class Consulta(Base):
    __tablename__ = "consultas"

    id          = Column(Integer, primary_key=True, autoincrement=True)
    wallet      = Column(String, nullable=False)
    token       = Column(String, nullable=False)
    saldo       = Column(Float, nullable=False)
    coletado_em = Column(DateTime, default=datetime.utcnow)