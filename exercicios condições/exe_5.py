num1 = int(input("insira o primeiro numero "))
num2 = int(input("insira o segundo numero "))

print("O que deseja fazer?")
print("1 - Somar")
print("2 - Subtrair")
print("3 - Dividir")
print("4 - Multiplicar")

operacao = int(input("Escolha uma das opções "))

match operacao:
    case 1:
        print(f"O resultado da soma é: {num1 + num2}")
    case 2:
        print(f"O resultado da subtração é: {num1 - num2}")
    case 3:
        if num2 != 0:  # Evitar divisão por zero
            print(f"O resultado da divisão é: {num1 / num2}")
        else:
            print("Não é possível dividir por zero.")
    case 4:
        print(f"O resultado da multiplicação é: {num1 * num2}")
    case _:
        print("Escolha uma das opções disponíveis.")