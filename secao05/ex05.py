"""
5. Faça um programa que receba um número inteiro e verifique se este número é par ou
ímpar.
"""
x = int(input("Digite o valor de x: "))

if (x % 2 == 0): # Resto da divisão
  print(f'O valor que foi digitado ele é PAR')
else:
  print(f'O valor que foi digitado ele é IMPAR')
