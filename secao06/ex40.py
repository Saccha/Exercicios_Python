"""
40. Elabore um programa que faça leitura de vários números inteiros, até que se
digite um número negativo. O programa tem que retornar o maior e o menor
número lido.
"""
num = int(input("Digite um número: "))
if num > 0:
    maior = num
    menor = num
    while num >= 0:
        num = int(input("Digite um número: "))
        if num < 0:
            break
        elif num > maior:
            maior = num
        elif num < menor:
            menor = num
    print()
    print(f"O menor número digitado é {menor}")
    print(f"O maior número digitado é {maior}")
else:
    print("O número deve ser maior ou igual a zero")
