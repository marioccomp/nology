from pydantic import BaseModel, Field
from typing import Literal
from datetime import datetime

class CashbackRequest(BaseModel):
    tipo_cliente: Literal["VIP", "REGULAR"]
    valor_pago: float = Field(gt=0)

class CashbackResponse(BaseModel):
    cashback: float 
    tipo_cliente: Literal["VIP", "REGULAR"]
    valor_pago: float

class ConsultaResponse(BaseModel):
    ip: str
    tipo_cliente: str
    valor_pago: float
    cashback: float
    created_at: datetime

    class Config:
        from_attributes = True