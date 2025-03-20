cot_dolar = float(input("Digite a cotação do dólar em reais "))

valor_dolar = float(input("Digite o valor em dólares a ser convertido "))

valor_real = cot_dolar * valor_dolar

print(f"O valor de ${valor_dolar:.2f} convertido para reais é R${valor_real:.2f}")
