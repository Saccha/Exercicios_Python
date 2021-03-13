"""
15. Usando Switch, escreva um programa que leia um inteiro entre 1 e 7 e imprima o dia
da semana correspondente a este número. Isto é, domingo se 1, segunda-feira se 2, e
assim por diante.
"""

x = int(input("Digite um número de 1 à 7: "))

if (x < 1 or x > 7):
  print("Número inválido")

elif (x == 1):
  print('Domingo')
elif (x == 2):
  print('Segunda')
elif (x == 3):
  print('Terça')
elif (x == 4):
  print('Quarta')
elif (x == 5):
  print('Quinta')
elif (x == 6):
  print('Sexta')
elif (x == 7):
  print('Sábado')
