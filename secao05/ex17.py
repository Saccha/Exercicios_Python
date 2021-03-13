"""
17. Faça um programa que calcule e mostre a área de um trapézio. Sabe-se que:
A = ((basemaior + basemenor) * altura) / 2
Lembre-se a base maior e a base menor devem ser números maiores que zero.
"""

base_maior = float(input("Digite o valor da base maior: "))
base_menor = float(input("Digite o valor da base menor: "))
altura = float(input("Digite o valor da altura: "))
area_total = ((base_maior + base_menor) * altura) / 2

if base_maior <= 0 or base_menor <= 0:
    print("Insira um número maior que 0.")
else:
    print(f"A área total do trapézio será de {area_total}.")
