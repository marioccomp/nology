from fastapi import APIRouter, Depends, Request
from sqlalchemy.orm import Session

from database import get_db
from schemas.cashback import CashbackRequest, CashbackResponse, ConsultaResponse
from services.cashback_service import calcular_cashback
from repositories.cashback_repository import salvar_consulta, listar_ultimas_consultas

router = APIRouter(prefix="/cashback", tags=["Cashback"])

@router.post("/calcular", response_model=CashbackResponse)
def calcular(request_data: CashbackRequest, request: Request, db: Session = Depends(get_db)):
    ip = request.client.host

    resultado = calcular_cashback(
        tipo_cliente=request_data.tipo_cliente,
        valor_pago=request_data.valor_pago,
    )

    salvar_consulta(db, resultado, ip)

    return resultado


@router.get("/listar", response_model=list[ConsultaResponse])
def listar_consultas(request: Request, db: Session = Depends(get_db)):
    ip = request.client.host
    return listar_ultimas_consultas(db, ip)    
