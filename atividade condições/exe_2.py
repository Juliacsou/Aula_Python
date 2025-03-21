bloco = int(input("Digite o número do seu bloco (1-20): "))

if bloco < 1 or bloco > 20:
    print("Bloco inválido! Digite um número entre 1 e 20.")

if bloco <= 10:
    print("O síndico responsável pelo seu bloco é o Sr. José.")
else:
    print("O síndico responsável pelo seu bloco é o Sr. Hamilton.")