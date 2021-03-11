""" 15. Leia um ângulo em radianos e apresente-o convertido em graus. A fórmula de conversão
é: G = R*180/þ, sendo G o ângulo em graus, R em radianos e þ em pi."""
import math

r = int(input("Digite o valor em radianos: "))
g = r * 180 / math.pi
print("%.4f" % g)
