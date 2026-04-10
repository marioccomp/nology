from models import ConsultaCashback
from sqlalchemy.orm import Session

def salvar_consulta(db: Session, dados: dict, ip: str):
    consulta = ConsultaCashback(
        ip=ip,
        tipo_cliente=dados["tipo_cliente"],
        cashback=dados["cashback"],
        valor_pago=dados["valor_pago"]
    )

    db.add(consulta)
    db.commit()
    db.refresh(consulta)

    return consulta

def listar_ultimas_consultas(db: Session, ip: str, limite: int = 10):
    return (
        db.query(ConsultaCashback)
        .where(ConsultaCashback.ip == ip)
        .order_by(ConsultaCashback.created_at.desc())
        .limit(limite)
        .all()
    )