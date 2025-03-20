percentual_distribuidor = 28 / 100
percentual_impostos = 45 / 100

custo_fabrica = float(input("Digite o custo de fábrica do carro "))

valor_distribuidor = custo_fabrica * percentual_distribuidor
valor_impostos = custo_fabrica * percentual_impostos

custo_final = custo_fabrica + valor_distribuidor + valor_impostos

print(f"O custo final do carro ao consumidor é de R$ {custo_final:.2f}")