'''
30.Faça uma função que receba como parâmetro o valor de um ângulo em graus e calcule o valor do coseno hiperbólico
desse ângulo usando sua respectiva série de Taylor. Considerar pi = 3.141593 e n variando de 0 a 5.
'''
import math as m
def serie_taylor(num):
    num = (3.141593)*num/180
    cos_hip = 0
    for i in range(0, 6):
        cos_hip += (num**(2*i))/m.factorial(2*i)
    return round(cos_hip, 3)
num = int(input("Digite um número: "))
serie_taylor(num)
