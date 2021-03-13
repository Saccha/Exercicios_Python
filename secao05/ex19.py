"""
19. Faça um programa para verificar se um determinado número inteiro é divisível por 3 ou 5,
mas não simultaneamente pelos dois.
"""

numero = int(input("Digite um número inteiro: "))

por_3 = numero % 3
por_5 = numero % 5

if por_3 == 0 and por_5 == 0:
    print("Pelos dois não pode.")
elif por_3 == 0:
    print("É divisível por 3.")
elif por_5 == 0:
    print("É divisível por 5.")
else:
    print("Tente novamente.")
