def calcular_cashback(tipo_cliente: str, valor_pago: float):
    cashback_base = valor_pago * 0.05
    cashback_final = cashback_base
    if tipo_cliente == "VIP":
        cashback_final += cashback_final * 0.10
    if valor_pago > 500:
        cashback_final *= 2
    return {
        "tipo_cliente": tipo_cliente,
        "cashback": round(cashback_final, 2),
        "valor_pago": valor_pago
    }