'''
35.Faça uma função não-recursiva que receba um número inteiro positivo n e retorne o fatorial quádruplo desse número.
O fatorial quádruplo de um número n é dado por: (2n)!/n!
'''
def quadruplo(numero):
    num = 1
    deno = 1
    for i in range(1, 2*num +1):
        num *= i
    for i in range(1, num+1):
        deno *= i
    return num/deno

num = int(input("Digite um número: "))
print(f"\nFatorial quadruplo de {num}: {quadruplo(num)}")
