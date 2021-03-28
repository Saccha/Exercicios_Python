'''
28.Faça uma função que receba como parâmetro o valor de um ângulo em graus e calcule o valor do coseno desse
ângulo usando sua respectiva série de Taylor. Considerar pi = 3.141593 e n variando de 0 a 5.
'''

from math import factorial
def cosseno(angulo):
    if angulo > 0:
        pi = 3.141593
        x = angulo * pi / 180
        cos = 0
        for n in range(6):
            numerador = x ** (2 * n)
            denominador = factorial(2 * n)
            cos += (-1) ** n / denominador * numerador
        return f"{angulo}° em radianos: {x}" \
               f"\nCosseno de {x}: {cos}"
    return "Valor inválido"
angulo = int(input("Digite o valor do ângulo em graus: "))
print(f"\n{cosseno(angulo)}")
