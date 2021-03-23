"""
27. Em Matemática, o número harmônico designado por H(n) define-se
como sendo a soma da série harmônica:
    H(n) = 1 + 1/2 + 1/3 + 1/4 + ... + 1/n
Faça um programa que leia um valor n inteiro e positivo e apresente o valor de H(n).
"""
num = int(input("Digite um número: "))
h = 1
if num > 0:
    for i in range(1,1+num):
        h += 1/i
    print(f'O valor de H(n): {h}')
else:
    print('O valor tem que ser positivo')
