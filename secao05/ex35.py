"""
35. Leia uma data e determine se ela é válida. Ou seja, verifique se o mês está entre 1 e 12,
e se o dia existe naquele mês. Note que Fevereiro tem 29 dias em anos bissextos, e 28
dias em anos não bissextos.
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
