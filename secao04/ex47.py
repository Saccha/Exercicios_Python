"""
47 - Leia um número inteiro de 4 dígitos (de 1.000 a 9.999) e imprima 1 dígito
por linha.
"""
inteiro = int(input("Digite um número inteiro de 1.000 a 9.999: "))

digito0 = str(inteiro)[0]
digito1 = str(inteiro)[1]
digito2 = str(inteiro)[2]
digito3 = str(inteiro)[3]
print(f"Este é o número que você digitou: {inteiro}")
print("E aqui é ele separado:")
print(digito0)
print(digito1)
print(digito2)
print(digito3)
