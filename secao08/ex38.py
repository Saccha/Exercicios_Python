'''
38.Faça uma função não-recursiva que receba um número inteiro positivo n e retorne o fatorial exponencial desse número. Um 
fatorial exponencial é um inteiro positivo n elevado à potência (n-1), que por sua vez é elevado à potência (n-2), e 
assim em diante
'''
def exponencial(num):
    prod = num
    for i in range(1, num):
        prod = prod**(num-i)
    return prod

num = int(input("Digite um número: "))
print(f"\nO fatorial exponencial de {num}: {exponencial(num)}")
