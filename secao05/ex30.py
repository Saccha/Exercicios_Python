"""
30. Faça um programa que receba três números e mostre-os em ordem crescente.
"""

numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))
numero3 = int(input("Digite o terceiro número: "))

lista = [numero1, numero2, numero3]

print(lista.sort())
print(lista)
