'''
37.Faça uma função não-recursiva que receba um número inteiro positivo n e retorne o hiperfatorial desse número. O 
hiperfatorial de um número n, escrito H(n), é definido por: H(n) = 1¹ * 2² * 3³ * ... * n^n.
'''
def hiperfatorial(num):
    prod = 1
    for i in range(1, num+1):
        prod *= i**i
    return prod

print(hiperfatorial(5))
