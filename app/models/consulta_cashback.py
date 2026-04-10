from sqlalchemy import Column, Integer, String, Float, DateTime
from datetime import datetime
from database import Base

class ConsultaCashback(Base):
    __tablename__ = "consultas"

    id = Column(Integer, primary_key=True, index=True)
    ip = Column(String, nullable=False)
    tipo_cliente = Column(String, nullable=False)
    valor_pago = Column(Float, nullable=False)
    cashback = Column(Float, nullable=False)
    created_at = Column(DateTime, default=datetime.now)