""" 14. Leia um ângulo em graus e apresente-o convertido em radianos. A fórmula de conversão
é: R = G * þ/180, sendo G o ângulo em graus e R em radianos e 3.14. # {þ = pi} """

import math
p = math.pi
g = float(input("Ângulo da Conversão: "))
r = float(g * p / 180)
print("%.4f" % r)
