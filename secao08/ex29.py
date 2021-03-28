'''
29.Faça uma função que receba como parâmetro o valor de um ângulo em graus e calcule o valor do seno hiperbólico
desse ângulo usando sua respectiva série de Taylor. Considerar pi = 3.141593 e n variando de 0 a 5.
'''

import math as m

def serie_taylor(num):
    num = (3.141593)*num/180
    senoh = 0
    for i in range(0, 6):
        senoh += (num**(2*i + 1))/m.factorial(2*i + 1)
    return round(senoh, 3)

print(serie_taylor(30))
