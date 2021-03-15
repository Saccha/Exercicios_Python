"""
31. Faça um programa que receba a altura e o peso de uma pessoa. De acordo com a tabela
a seguir, verifique e mostra qual classificação dessa pessoa.
** TABELA NA FOLHA DE EXERCICIOS DA SEÇÃO 5 **
"""

altura = float(input("Digite a altura em metros: "))
peso = float(input("Digite o peso em KG: "))

if altura < 1.20 and 0 <= peso < 60:
    print("A")
elif 1.20 <= altura <= 1.70 and 0 <= peso < 60:
    print("B")
elif altura > 1.70 and 0 <= peso < 60:
    print("C")
elif altura < 1.20 and 60 <= peso <= 90:
    print("D")
elif 1.20 <= altura <= 1.70 and 60 <= peso >= 90:
    print("E")
elif altura > 1.70 and 60 <= peso <= 90:
    print("F")
elif altura < 1.20 and peso > 90:
    print("G")
elif 1.20 <= altura <= 1.70 and peso > 90:
    print("H")
elif altura > 1.70 and peso > 90:
    print("I")
else:
    print("Iválido.")
