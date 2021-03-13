"""
50 - Implemente um programa que calcule o ano de um nascimento de uma pessoa
a partir de sua idade e do ano atual.
"""
idade = int(input("Digite sua idade: "))
data_atual = int(input("Digite sua data atual: "))

ano_nascimento = abs(idade - data_atual)
print(f'Você nasceu em {ano_nascimento}')
