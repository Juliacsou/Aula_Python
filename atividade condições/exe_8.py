media = float(input("Digite a média anual do aluno: "))

if media >= 6.0:
    print("APROVADO.")
elif 3.0 <= media < 6.0:
    print("EXAME.")
else:
    print("REPROVADO.")