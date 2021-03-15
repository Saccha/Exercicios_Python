"""
38. Leia uma data de nascimento de uma pessoa fornecida através de três números inteiros:
Dia, Mês e Ano. Teste a validade desta data para saber se está é uma data válida. Teste
se o dia fornecido é um dia válido: dia > 0, dia <= 28 para o mês de fevereiro (29 se o
ano for bissexto), dia <= 30 em abril, junho, setembro e novembro , dia <= 31 nos outros
meses. Teste a validade de mês: mês > 0 e mês < 13. Teste a validade do ano: ano <=
ano atual (use uma constante definida com o valor igual a 2008). Imprimir: "data válida"
ou "data inválida" no final da execução do programa.
"""
dia = int(input("Digite o dia: "))
mes = int(input("Digite o mês: "))
ano = int(input("Digite o ano: "))

if 1 <= dia <= 31 and (mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12):
    print("Data válida.")
elif 1 <= dia <= 30 and (mes == 4 or mes == 6 or mes == 9 or mes == 11):
    print("Data válida.")
elif mes == 2 and (ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0):
    print("Data válida.")
elif mes == 2 and (1 <= dia <= 28):
    print("Data válida.")
else:
    print("Data inválida.")
