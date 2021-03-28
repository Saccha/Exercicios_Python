'''
27.Faça uma função que receba como parâmetro o valor de um ângulo em graus e calcule o valor do seno desse
ângulo usando sua respectiva série de Taylor. Considerar pi = 3.141593 e n variando de 0 a 5.
'''
import math as m
def seno(num):
  num = (3.141593)*num/100
  seno = 0
  for i in range(0,6):
    seno += ((-1)**i)/m.factorial(2*i+1) * (num**(2*i+1))
  return round(seno,3)
num = int(input("Digite um número: "))
print(f"\n{seno(num)}")
