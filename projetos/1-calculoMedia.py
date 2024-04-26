print("..........................")
print("CALCULANDO A MEDIA DE NOTA")

materia = input("Digita a Materia: ")
notaA = float(input("Digita sua nota dos Exercicios."))
notaB = float(input("Digita sua nota do Portifolio."))
notaC = float(input("Digita sua nota da Prova."))
notaMedia = 7

calculoMedia = (notaA + notaB + notaC) / 3
print("Sua Média é: %.2f" % calculoMedia)

if calculoMedia >= 7 and calculoMedia < 8:
    print("PARABÉNS, Você foi REPROVADO(a), GANHOU uma BOLSA de 10%. ")
elif calculoMedia >= 8 and calculoMedia < 9:
    print("EXCELENTE, Você foi APROVADO(a), GANHOU uma BOLSA de 50%. ")
elif calculoMedia >= 9 and calculoMedia <= 10:
    print("SENSACIOANL, você foi aprovado(a), GANHOU UMA BOLSA de 80%. ")
else:
    print("INFELIZMENTE, você não foi APROVADO(a), ESTUDE MAIS. ")

print(" FIM DA PROGRAMA ")
print("..........................")