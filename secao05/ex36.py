"""
36. Escreva um program que, dado o valor da venda, imprima a comissão que deverá ser
paga ao vendedor. Para calcular a comissão, considere a tabela abaixo:
** TABELA NA FOLHA DE EXERCICIOS DA SEÇÃO 5 **
"""
valor_da_venda = float(input("Digite o valor da venda: "))

if valor_da_venda >= 100_000:
    valor_final = 700 + (valor_da_venda * (116/100))
    print(f"O valor final com comissão é R${valor_final}")

elif 100_000 > valor_da_venda >= 80_000:
    valor_final = 650 + (valor_da_venda * (114/100))
    print(f"O valor final com comissão é R${valor_final}")

elif 80_000 > valor_da_venda >= 60_000:
    valor_final = 600 + (valor_da_venda * (114/100))
    print(f"O valor final com comissão é R${valor_final}")

elif 60_000 > valor_da_venda >= 40_000:
    valor_final = 550 + (valor_da_venda * (114/100))
    print(f"O valor final com comissão é R${valor_final}")

elif 40_000 > valor_da_venda >= 20_000:
    valor_final = 500 + (valor_da_venda * (114/100))
    print(f"O valor final com comissão é R${valor_final}")

elif valor_da_venda > 20_000:
    valor_final = 400 + (valor_da_venda * (114/100))
    print(f"O valor final com comissão é R${valor_final}")
