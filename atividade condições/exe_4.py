horas = int(input("Digite o número de horas de permanência: "))

a_pagar = horas * 5

if a_pagar > 35:
    a_pagar = 35

print(f"O total a pagar é R$ {a_pagar:.2f}")