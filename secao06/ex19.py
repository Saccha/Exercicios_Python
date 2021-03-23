"""
19.Escreva um algoritmo que leia um número inteiro entre 100 e 999 e imprima na saída
cada um dos algarismos que compõem o número
"""
numero = int(input("Digite um número entre 100 e 999: "))

if 100 <= numero <= 999:
    centena = numero // 100 % 10
    dezena = numero // 10 % 10
    uidade = numero // 1 % 10

    print("O algarismos são:")
    print(f"Centena: {centena}")
    print(f"Dezena: {dezena}")
    print(f"Unidade: {uidade}")
