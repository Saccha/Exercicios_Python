"""
40. O custo ao consumidor de um carro novo é a soma do custo de fábrica, da comissão
do distribuidor, e dos impostos. A comissão e os impostos são calculados sobre o custo
de fábrica, de acordo com a tabela abaixo. Leia o custo de fábrica e escreva o custo ao
consumidor.
** TABELA NA FOLHA DE EXERCICIOS DA SEÇÃO 5 **
"""
preco_carro = float(input("Digite o preço do carro, R$ "))

if preco_carro <= 12_000:
    comissao_do_distribuidor = preco_carro * (5/100)
    imposto = 0
    print(f"O preço final do carro será R${preco_carro + comissao_do_distribuidor + imposto}")

elif 12_000 < preco_carro <= 25_000:
    comissao_do_distribuidor = preco_carro * (10/100)
    imposto = preco_carro * (15/100)
    print(f"O preço final do carro será R${preco_carro + comissao_do_distribuidor + imposto}")

elif preco_carro > 25_000:
    comissao_do_distribuidor = preco_carro * (15/100)
    imposto = preco_carro * (20/100)
    print(f"O preço final do carro será R${preco_carro + comissao_do_distribuidor + imposto}")
