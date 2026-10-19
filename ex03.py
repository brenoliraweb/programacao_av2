# Crie uma função para calcular frete que receba: distancia e peso. Retorne o valor do
# frete baseado em regras:
# · até 100 km -> 1.50 * peso (1.50 R$)
# acima de 100 km -> 2 * peso (2 R$)

def calcular_frete(distancia, peso):
    if distancia <= 100:
        valor_frete = 1.5 * peso
        return valor_frete
    else:
        valor_frete = 2 * peso
        return valor_frete

print(calcular_frete(100, 1000))
