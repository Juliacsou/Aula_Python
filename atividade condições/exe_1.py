bloco = int(input("Digite o número do seu bloco: "))

if bloco < 1 or bloco > 4:
    print("Bloco inválido!")

if bloco % 2 == 0:
    print("Seu bloco é abastecido pela Caixa A.")
else:
    print("Seu bloco é abastecido pela Caixa B.")
