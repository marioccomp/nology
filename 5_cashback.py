
# Aqui eu criei uma função que calcula o valor final já considerando o desconto, para que a função de calcular o cashback não tenha esse papel

def calcular_valor_final(valor_total: float, desconto_percentual: float):
     return valor_total * (1 - desconto_percentual)


def calcular_cashback(valor_final: float, vip: bool): 
        cashback_base = 0.05 * valor_final  # Cashback base é 5% do valor pago
        cashback_final = cashback_base
        if vip: 
            cashback_final += cashback_base * 0.10  # Se for vip, o cashback final vai ser o cashback base + 10% do cashback base
        if valor_final > 500:
            cashback_final *= 2 # Caso o valor pago tenha sido maior que R$ 500, o cashback é dobrado
        
        print(f"Cashback gerado: R$ {cashback_final:.2f}")
        return cashback_final

calcular_cashback(calcular_valor_final(600, 0.20), True)
calcular_cashback(calcular_valor_final(600, 0.1), False)
calcular_cashback(calcular_valor_final(600, 0.15), True)


