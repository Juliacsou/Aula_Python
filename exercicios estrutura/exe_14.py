salario_fixo = float(input("Digite o salário fixo do vendedor "))
comissao = float(input("Digite o valor da comissão por carro vendido "))
carros_vendidos = int(input("Digite o número de carros vendidos "))
total_vendas = float(input("Digite o valor total das vendas "))

comissao_total = carros_vendidos * comissao
porcentagem_vendas = total_vendas * 0.05
salario_final = salario_fixo + comissao_total + porcentagem_vendas

print(f"O salário final do vendedor é de R$ {salario_final:.2f}")