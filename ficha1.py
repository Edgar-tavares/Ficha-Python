# -*- coding: utf-8 -*-
"""

LISTA DE EXERCÍCIOS DE ALGORITMOS CONDICIONAIS

1) Faça um algoritmo que leia os valores A, B, C e imprima na tela se a soma de A + B é menor
que C.
"""

a = 2
b = 5
c = 7
if a + b < c:
  print("A soma de A + B é menor que C")
else:
   print("A soma de A + B não é menor que C")

"""2) Faça um algoritmo que leia o nome, o sexo e o estado civil de uma pessoa. Caso sexo seja “F” e
estado civil seja “CASADA”, solicitar o tempo de casada (anos).
"""

nome = "Maria"
sexo = "F"
estado_civil = "casada"

if sexo == "F" and estado_civil == "casada":
  print("Você está casada a quantos anos?")

"""3) Faça um algoritmo para receber um número qualquer e informar na tela se é par ou ímpar."""

num = int(input('Digite um número: '))
if num % 2 == 0:
  print(f'O número {num} é par')
else:
  print(f'O número {num} é ímpar')

"""4) Faça um algoritmo que leia dois valores inteiros A e B se os valores forem iguais deverá se
somar os dois, caso contrário multiplique A por B. Ao final de qualquer um dos cálculos deve-se
atribuir o resultado para uma variável C e mostrar seu conteúdo na tela.
"""

a = 5
b = 7
if a == b:
  c = a + b
  print(c)
else:
  c = a * b
  print(c)

"""5) Encontrar o dobro de um número caso ele seja positivo e o seu triplo caso seja negativo,
imprimindo o resultado.
"""

a = -2
if a > 0:
  print(a * 2)
else:
  print(a * 3)

"""6) Escreva um algoritmo que lê dois valores booleanos (lógicos) e então determina se ambos são
VERDADEIROS ou FALSOS.
"""

a = True
b = False
if a == True and b == True:
  print("Os dois valores são verdadeiros")
else:
  print("Os dois valores são falsos")

"""7) Faça um algoritmo que leia uma variável e some 5 caso seja par ou some 8 caso seja ímpar,
imprimir o resultado desta operação.
"""

a = 2
if a % 2 == 0:
  print(a + 5)
else:
  print(a + 8)

"""8) Escreva um algoritmo que leia três valores inteiros e diferentes e mostre-os em ordem
decrescente.
"""

a = 2
b = 5
c = 7
if a > b and a > c:
  print(a)

"""9) Tendo como dados de entrada a altura e o sexo de uma pessoa, construa um algoritmo que
calcule seu peso ideal, utilizando as seguintes fórmulas:
● para homens: (72.7 * h) – 58;
● para mulheres: (62.1 * h) – 44.7.
"""

altura = 1.70
sexo = "M"
if sexo == "M":
  peso_ideal = (72.7 * altura) - 58
  print(peso_ideal)

"""10) O IMC – Indice de Massa Corporal é um critério da Organização Mundial de Saúde para dar
umaindicação sobre a condição de peso de uma pessoa adulta. A fórmula é IMC = peso / ( altura )2
Elabore um algoritmo que leia o peso e a altura de um adulto e mostre sua condição de acordo
com a tabela abaixo.
"""

imc = 20

if imc < 18.5:
    print("Abaixo do peso")
elif 18.5 <= imc <= 25:
    print("Peso normal")
elif 25 < imc <= 30:
    print("Acima do peso")
else:
    print("Obesidade")
