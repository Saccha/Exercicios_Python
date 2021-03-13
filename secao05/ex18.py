"""
18. Faça um programa que mostre ao usuário um menu com 4 opções de operações
matemáticas (as básicas, por exemplo). O usuário escolhe uma das opções e
o seu programa então pede dois valores numéricos e realiza a operação,
mostrando o resultado e saindo.
"""

print("1 > SOMA")
print("2 > SUBTRAÇÃO")
print("3 > MULTIPLICAÇÃO")
print("4 > DIVISÃO")

operacoes = int(input("Escolha o operador entre entre 1 e 4: "))

if operacoes == 1:
    print("Você escolheu SOMAR.")
elif operacoes == 2:
    print("Você escolheu SUBTRAIR.")
elif operacoes == 3:
    print("Você escolheu MULTIPLICAR.")
elif operacoes == 4:
    print("Você escolheu DIVIDIR.")

valor1 = int(input("Digite o primeiro valor: "))
valor2 = int(input("Digite o segundo valor: "))

if operacoes == 1:
    resultado = valor1 + valor2
    print(resultado)
elif operacoes == 2:
    resultado = valor1 - valor2
    print(resultado)
elif operacoes == 3:
    resultado = valor1 * valor2
    print(resultado)
elif operacoes == 4:
    resultado = valor1 / valor2
    print(resultado)
