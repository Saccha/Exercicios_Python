"""
7. Faça um programa que receba dois números e mostre o maior. Se por acaso, os dois
números forem iguais, imprima a mensagem NÚMEROS IGUAIS.
"""
x = int(input("Digite o valor de x: "))
y = int(input("Digite o valor de y: "))

if (x > y):
  dif = x - y
  print(f'O maior número será {x}, e a diferença entre eles será de {dif}.')
elif (y > x):
  dif = y - x
  print(f'O maior número será {y}, e a diferença entre eles será de {dif}.')
else:
  print('Números Iguais.')
