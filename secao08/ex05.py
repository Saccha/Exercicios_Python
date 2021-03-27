"""
5.Faça uma função e um programa de teste para o cálculo do volume
de uma esfera. Sendo que o raio é passado por parâmetro.
V = 4/3 * r * R³
"""
from math import pi

def esfera(raio):
  return (4/3) * pi * (raio ** 3)
x = int(input("Digite o raio da esfera: "))
print(f'\nVolume da esfera: {esfera(x)}')
