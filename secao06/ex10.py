'''
10. Faça um programa que calcule e mostre a soma dos 50 primeiros números pares.
'''
a1 = int(input('Digite o a1: '))
n = int(input('Digite o n: '))
r = int(input('Digite o r: '))

an = a1 + ((n - 1) * r)

sn = (((a1 + an) * n) / 2)

print(an, sn)
