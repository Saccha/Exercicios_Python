"""
23) Faça um algoritmo que leia um número positivo e imprima seus divisores.
"""
x = int(input('Digite um número: '))
if x > 0:
  print('Os divisores desse número são: ')
  for i in range(1,1+x):
    if x % i == 0:
      print(i)
else:
  print('O número deve ser positivo!')
