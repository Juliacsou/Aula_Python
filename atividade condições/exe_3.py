valor_merc = float(input("Digite o valor da mercadoria: "))
valor_disp = float(input("Digite o valor que você tem: "))

if valor_disp >= valor_merc:
    print("Você tem dinheiro suficiente para comprar.")
else:
    print("Você NÃO tem dinheiro suficiente para comprar.")