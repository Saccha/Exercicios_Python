"""
32. Escrever um programa que leia o código do produto escolhido do cardápio de uma lan-
chonete e a quantidade. O programa deve calcular o valor a ser pago por aquele lanche.
Considere que a cada execução somente será calculado um pedido. O cardápio da lan-
chonete segue o padrão da tabela abaixo:
** TABELA NA FOLHA DE EXERCICIOS DA SEÇÃO 5 **
"""

codigo_produto = int(input("Digite o código do produto: "))

if codigo_produto == 100:
    preco_unitario = 1.20
    qtde = int(input("Digite a quantidade de Cachorros-Quente: "))
    preco_total = preco_unitario * qtde
    print(preco_total)

elif codigo_produto == 101:
    preco_unitario = 1.30
    qtde = int(input("Digite a quantidade de Baurus Simples: "))
    preco_total = preco_unitario * qtde
    print(preco_total)

elif codigo_produto == 102:
    preco_unitario = 1.50
    qtde = int(input("Digite a quantidade de Baurus com Ovos: "))
    preco_total = preco_unitario * qtde
    print(preco_total)

elif codigo_produto == 103:
    preco_unitario = 1.20
    qtde = int(input("Digite a quantidade de Hamburgues: "))
    preco_total = preco_unitario * qtde
    print(preco_total)

elif codigo_produto == 104:
    preco_unitario = 1.70
    qtde = int(input("Digite a quantidade de Cheeseburguers: "))
    preco_total = preco_unitario * qtde
    print(preco_total)

elif codigo_produto == 105:
    preco_unitario = 2.20
    qtde = int(input("Digite a quantidade de Sucos: "))
    preco_total = preco_unitario * qtde
    print(preco_total)

elif codigo_produto == 106:
    preco_unitario = 1.00
    qtde = int(input("Digite a quantidade de Refrigerantes: "))
    preco_total = preco_unitario * qtde
    print(preco_total)

else:
    print("Digite um produto válido.")
