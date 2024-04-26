# INSTALANDO PACOTES NO PYTHON
""" pip install <NOME DO PACOTE> """

# -------------------------------------------------------------#
# TIPOS DE COMENTARIOS

# ALTA + SHIFT + A = COMENTA O TEXTO INTEIRO VARIAS LINHAS
""" ADICIONA SEU COMENTARIO AQUI
ADICIONA SEU COMENTARIO AQUI
ADICIONA SEU COMENTARIO AQUI
ADICIONA SEU COMENTARIO AQUI """

# CTRL + K = COLOCA O COMENTARIO ATE O FINAL DA LINHA
# CTRL + C = TIRAR O COMENTARIO ATE O FINAL DA LINHA

# ADICIONA SEU COMENTARIO AQUI
X = 10 # ADICIONA SEU COMENTARIO AQUI

# -------------------------------------------------------------#
# VARIAVEL 'espaço' EM MEMORIA, PARA GUARDAR UM VALOR DURANTE A EXECUÇÃO
# TIPOS DE VARIAVEIS

""" 
Texto String ('Douglas') Ex: Nome
Inteiro int (18) Ex: Idade
Float (3.5) Ex: Altura
Booleans bool (True or False) Transação Fraudulenta

Declaração de variavies no Python é implicita: Fracamente tipada.

 """
# variavel tipo inteiro
""" x = 1 """
# variavel tipo float
""" y = 3.13 """
# variavel tipo string
""" z = "python"
    y = 'python' 
"""
# variavel tipo logica
""" w = true
    y = false
"""
# -------------------------------------------------------------#
# PRINCIPAIS OPERADORES
""" 
+ = SOMA
- =  SUBTRAÇÃO
/ =  DIVISAO
* = MULTIPLICAÇÃO
** = EXPONENCIAÇÃO
% = OPERADORES DE MODULO
"""
# -------------------------------------------------------------#
# EXIBIR VALORES NA TELA
""" 
print("Hello World!")
print(x)
priny("Hello world", x, y) 
"""
# -------------------------------------------------------------#
# VERIFICACAO DE TIPOS
""" 
x = 10
type (x)
print(type(x))

x = '10'
type (x)
print(type(x))

x = 10.1
type (x)
print(type(x))

x = True
type (x)
print(type(x))

<class 'int'>
<class 'str'>
<class 'float'>
<class 'bool'>

"""
# -------------------------------------------------------------#
# ENTRADA DE VALORES
""" 
x = input('Digita seu primeiro nome:')
y = input('Digita seu segundo nome:')
z = x+y
print(z)

x = int (input('Digita um valor 1:'))
y = int (input('Digita um valor 2:'))
z = (x + y)
print(z)

"""
# -------------------------------------------------------------#
# CONVERSAÕES DE VALORES

""" 
x = int(z)
x = str(z)
x = float(z)

"""
# -------------------------------------------------------------#
# ESTRUTURA DE DECISÃO

"""
IF = SE
ELIF = SE ENTAO
ELSE  = ENTAO

"""
""" 
if (condicao logica):
    // EXECUTA SE FOR VERDADEIRO
    // EXECUTA SE FOR VERDADEIRO
    // EXECUTA SE FOR VERDADEIRO
    
elif (condicao logica)
    // bloco de codigo
    // bloco de codigo
    // bloco de codigo
    
else:
    // EXECUTA SE FOR FALSO
    // EXECUTA SE FOR FALSO
    // EXECUTA SE FOR FALSO
"""
""" 
n1 = int(input('Digita o primeiro nota:'))
n2 = int(input('Digita o segundo nota:'))
n3 = int(input('Digita a terceira nota:'))

med = 7
res = (n1 + n2 + n3) / 3
print(res)

if res >= med:
    print('APROVADO')
elif res < 7 and res >= 5:
    print('RECUPERAÇÃO')
else:
    print('REPROVADO')

"""
# -------------------------------------------------------------#
# OPERADORES DE COMPARACAO
""" 
< NENOR QUE
> MAIOR QUE
<= MENOR OU IGUAL
>= MAIOR OU IGUAL
== IGUAL
!= DIFERENTE 

"""
# --------------------------------- #
# OPERADORES DE LOGICO
"""
AND =  E
OR =  OU
NOT =  NAO 

 """
# -------------------------------------------------------------#
# ESTRUTURA DE REPETIÇÃO
# DOIS TIPO PRINCIPAIS
    # EXECUTA ENQUANTO A CONDICAO LOGICA FOR VERDADEIRA
    # EXECUTA UM NUMERO "N" DE VEZES
"""
WHILE  = EM QUANTO
FOR = USA EM UM INTERVALO (0,10)

# INTERRUPÇÃO
BREAK = CANCELA O LAÇO
CONTINUE = REINICIA O LAÇO
 """

# EXEMPLO DE WHILE
""" 
count = 1
while count <=5:
    print(count)
    count += 1
"""
# EXEMPLO DE FOR
    # RANGE (0, 10, 1)
    # RANGE (INICIO, PARADA, INCREMETO)
    # INCREMENTO OPCIONAL, PODE SER NEGATIVO
 
# -------------------------------------------------------------#
# LISTA  = VETORES DE VALORES
# DADOS NAO PRECISA SER DO MESMO TIPOS
# ACESSO PRIMEIRO ELEMENTO  - INDEXADAS EM ZERO [0,1,2,3,4,5,6]
""" lst [0] """
# NUMERO DE ELEMENTOS EM UMA LISTA
""" len(lst) """

"""
1ST = [1,2,3,4,5] 
2ST = [1,2,3,4,5, "4", True]
3ST = [12,[1,2,3,4,5], "A"]
4ST = list (range(0,10))
 """
# -------------------------------------------------------------#
# ESTRUTURAS DE DADOS NO PYTHON
# DICIONARIOS = ARMAZENA ESTRUTURAS DE CHAVE E VALOR
    # CONJUNTO DE CHAVE/VALOR ASSOCIADOS
    # DECLARADOS POR CHAVES E SEPARADO POR DOIS PONTOS
    
""" precos = {"lapis":5.5, "borracha":7.0, "caneta":6.5} """

# -------------------------------------------------------------#
# ESTRUTURAS DE DADOS NO PYTHON
# SETS = ARMAZENA APENAS VALOR
    # CONJUNTO NAO ORDENADOS E NAO REPETIDOS DE ELEMENTOS

""" animais = {"gato","cachorro"} """

# -------------------------------------------------------------#
# ESTRUTURAS DE DADOS NO PYTHON
# TUPLAS = SÃO LISTA QUE NAO PODE SER ALTERADAS

""" tp1 = (1,2,3,4,5,6) """
 
# -------------------------------------------------------------#
# ENTENDENDO BIBLIOTECA  = NUMPY = USO MATEMATICOS

""" 
import numpy as np

a = np.array ([12,34,26,18,10])
print(a)
print(a.dtype)

"""

# -------------------------------------------------------------#
# https://docs.python.org/3/library

# MILHARES DE FUNÇÕES USADAS NO DIA A DIA QUE JA VEM COM PYTHON

""" 
FUNÇÕES MATEMATICAS
NUMEROS ALEATORIOS
CRIPTOGRAFIA
LEITURA DE ARQUIVOS
PROTOCOLO DE COMUNICAÇÃO

"""

# -------------------------------------------------------------#
# PITHON PACKAGING INDEX: https://pypi.org/
    # PIP É UM PROGRAMA PARA INSTALAR MODULOS E PACOTES.
    
# INSTALANDO O PIP
""" py -m ensurepip --upgrade """
""" py -m pip install --upgrade pip """

# INSTALANDO UM PACOTE
""" pip install numpy """
""" pip install panda """

# -------------------------------------------------------------#
# ENTENDENDO BIBLIOTECA  = PANDAS = 
    # DOIS OBJETOS = DATAFRAME / SERIES
""" 
import pandas as pd

dados = pd.read_csv('basecensus.csv')
print(dados)

"""

# -------------------------------------------------------------#
# MODULOS ADICIONAIS
    # CONJUNTO DE FUNCIONALIDADES ORGANIZADAS EM ARQUIVOS

""" 
import statistics

x = statistics.mean(z) # valor que quer calcular a media
y = statistics.median(z) # valor que quer calcular

"""

""" 
import statistics as sta

x = sta.mean(z) # valor que quer calcular a media
y = sta.median(z) # valor que quer calcular

"""

""" 
from statistics import mean, median
    mean()
    median()
or

from statistics import*

"""
    
# -------------------------------------------------------------#
# PACOTES ADICIONAIS = PACKAGES
    # CONJUNTO DE FUNCIONALIDADES ORGANIZADAS EM ARQUIVOS
    # PERMITE ORGANIZAR MODULOS USANDO UMA NOTACAO DE PONTOS
    
""" import ciencidados.estatisticas, cienciadedados.machinelearning  """

# -------------------------------------------------------------#
# FUNÇÕES SAO BLOCOS DE CODIGOS QUE PODEM SER USADOS VARIAS VEZES.
    # CRIAR UMA FUNÇÃO

""" 
def imprime ():
    print('Imprime essa funcao')

# Execuando Função
imprime ()
 """
 
""" 
def imprime (n):
    print(n)
    
    imprime('imprime o texto')
    
 """
 
""" 
def potencia (n):
    return n * n

x = potencia(3)
 
 """

# EXEMPLO COM VALOR DEFAUT
""" 
def intervalo (inic=1, fim=10)
    for inic in range(1, 10)
    print(inic)

intervalo(1, 10)
intervalo()
"""
# -------------------------------------------------------------#
# FUNÇÕES PADRÕES 

""" 
abs() valor absoluto
max() maximo
min() minimo
round() arredonda
sum() soma 
 """
 
# -------------------------------------------------------------#
# MODULOS NATIVOS
""" 
from statistics import*
mean() media
median() mediana
mode() modo
stdev() desvio padrao
variance() variancia
 """
# -------------------------------------------------------------#









