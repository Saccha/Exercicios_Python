"""
6. Escreva um programa que, dados dois números inteiros, mostre na tela o maior deles,
assim como a diferença existente entre ambos.
"""

x = int(input("Digite o valor de x: "))
y = int(input("Digite o valor de y: "))

if (x > y):
  dif = x - y
  print(f'O maior número será {x}, e a diferença entre eles será de {dif}.')
elif (y > x):
  dif = y - x
  print(f'O maior número será {y}, e a diferença entre eles será de {dif}.')
