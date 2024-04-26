# resultados menores que 16 — magreza grave;
# resultados entre 16 e 16,9 — magreza moderada;
# resultados entre 17 e 18,5 — magreza leve;
# resultados entre 18,6 e 24,9 — peso ideal;
# resultados entre 25 e 29,9 — sobrepeso;
# resultados entre 30 e 34,9 — obesidade grau I;
# resultados entre 35 e 39,9 — obesidade grau II ou severa;
# resultados maiores do que 40 — obesidade grau III ou mórbida.

# Fazer o cálculo do IMC é bem fácil. Primeiro, 
# você vai multiplicar o valor de sua altura (em metros) por ele mesmo. 
# Por exemplo, se você medir 1,60 metros, o cálculo será:
# 1,6 x 1,6 = 2,56

# Em seguida, é hora de trazer o seu peso para a equação. 
# Ele deverá ser dividido pelo valor obtido acima. 
# Pensando no mesmo exemplo anterior, se o seu peso for 60 quilos, a conta será:
# 60 ÷ 2,56 = 23,43
# Essa pessoa, portanto, tem um IMC considerado como sobrepeso.

print("--------------------------")
print("CALCULANDO SEU IMC")
print("--------------------------")
peso = float(input("1º Qual é seu peso? "))
altura = float(input("2º Qual é a sua altura? "))
imc = peso / (altura**2)
print("3º O IMC dessa pessoa é: %.1f " % imc)

if imc < 16:
    print("4º Magreza grave, CUIDADO III!")
elif 16 <= imc < 16.9:
    print("4º Magreza moderada, CUIDADO II")
elif 17 <= imc < 18.5:
    print("4º Magreza leve, CUIDADO I")
elif 18.6 <= imc < 24.9:
    print("4º Peso ideal, PARABÉNS!")
elif 25 <= imc < 29.9:
    print("4º Sobrepeso, ATENÇÃO, SE-CUIDE")
elif 30 <= imc < 34.9:
    print("4º Obesidade grau I, EXTREMO CUIDADO I!")
elif 35 <= imc < 39.9:
    print("4º Obesidade grau II ou severa, EXTREMO CUIDADO II!")
elif imc >= 40: 
    print("4º Obesidade grau III ou mórbida, EXTREMO CUIDADO III!")

print("--------------------------")
print(" FIM DO PROGRAMA ")
print("--------------------------")