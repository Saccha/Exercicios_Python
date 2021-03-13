"""
12. Ler um número inteiro. Se o número lido for negativo, escreva a mensagem "Número
inválido". Se o número for positivo, calcular o logaritmo deste número.
"""

import math

num = int(input("Digite um número inteiro: "))
if num < 0:
  print("Número inválido")
elif num > 0:
  num = math.log(num,10)  #math.log(VARIAVEL, BASE)
  print(num)
