anos = int(input("Digite a idade em anos "))
meses = int(input("Digite os meses adicionais "))
dias = int(input("Digite os dias adicionais "))

total_dias = (anos * 365) + (meses * 30) + dias

print(f"A idade em dias é de {total_dias} dias")