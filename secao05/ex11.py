"""
11. Escreva um programa que leia um número inteiro maior do que zero e devolva, na tela, a
soam de todos os seus algarismos. Por exemplo, ao número 251 corresponderá o valor
8 (2 + 5 + 1). Se o número lido não for maior do que zero, o programa terminará com a
mensagem "Número inválido".
"""
numero = str(input("Digite um número inteiro: "))

if int(numero) < 0:
    print("Número inválido.")
else:
    soma = 0
    for i in numero:
        soma += int(i)
    print(soma)
