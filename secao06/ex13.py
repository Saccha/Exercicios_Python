'''
13. Faça um programa que leia um número inteiro positivo par N e imprima todos os números pares de 0 até N em ordem
decrescente
'''
x = int(input("Digite um número qualquer: "))
y = 0
if x % 2 == 0:
  while y <= x:
    if y % 2 == 0:
      print(y)
    y += 1
else:
  print("Tem que ser valor par")
