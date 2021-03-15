"""
33. Um produto vai sofrer aumento de acordo com a tabela abaixo. Leia o preço antigo,
calcule e escreva o preço novo, e escreva uma mensagem em função do preço novo (de
acordo com a segunda tabela).
** TABELA NA FOLHA DE EXERCICIOS DA SEÇÃO 5 **
"""
preco_produto = float(input("Digite o preço do produto: "))

if preco_produto < 50:
    aumento = preco_produto + (preco_produto * (5/100))
    print(f"Com percentual de 5% fica R${aumento}")
elif 50 <= preco_produto < 100:
    aumento = preco_produto * (110/100)
    print(f"Com percentual de 10% fica R${aumento}")
elif preco_produto >= 100:
    aumento = preco_produto * (115/100)
    print(f"Com percentual de 15% fica R${aumento}")

if aumento < 80:
    print("Barato.")
elif 80 <= aumento <= 120:
    print("Normal.")
elif 120 <= aumento <= 200:
    print("Caro.")
elif aumento > 200:
    print("Muito Caro.")
