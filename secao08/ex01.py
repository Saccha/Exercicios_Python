"""
1.Crie uma função que recebe como parâmetro um número inteiro e devolve
o seu dobro.
"""

def dobro(num):
  if num // 1 == num:
    return num * 2
x = float(input("Digite um número: "))
print(f'\nDobro de {x}: {dobro(x)}')
