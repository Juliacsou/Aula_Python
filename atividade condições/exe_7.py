quant = int(input("Digite o número de maçãs compradas: "))

if quant >= 12:
    preco_maca = 1.00
else:
    preco_maca = 1.30

total = quant * preco_maca

print(f"O total a pagar é R$ {total:.2f}")