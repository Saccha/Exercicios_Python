"""
16. Usando Switch, escreva um programa que leia um inteiro entre 1 e 12 e imprima o mês
correspondente a este número. Isto é, janeiro se 1, fevereiro se 2, e assim por diante.
"""
x = int(input("Digite um número de 1 à 12: "))

if (x < 1 or x > 12):
  print("Número inválido")

elif (x == 1):
  print('Janeiro')
elif (x == 2):
  print('Fevereiro')
elif (x == 3):
  print('Março')
elif (x == 4):
  print('Abril')
elif (x == 5):
  print('Maio')
elif (x == 6):
  print('Junho')
elif (x == 7):
  print('Julho')
elif (x == 8):
  print('Agosto')
elif (x == 9):
  print('Setembro')
elif (x == 10):
  print('Outubro')
elif (x == 11):
  print('Novembro')
elif (x == 12):
  print('Dezembro')
