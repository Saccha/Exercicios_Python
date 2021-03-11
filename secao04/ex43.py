#43. Escreva um programa de ajuda para vendedores. A partir de um valor total lido, mostre:
#    * O total a pagar com desconto de 10%;
#    * O valor de cada parcela, no parcelamento de 3x sem juros;
#    * A comissão do vendedor, no caso da venda ser a vista(5% sobre o valor com des-
#      conto)
#    * A comissão do vendedor,no caso ser parcelada (5% sobre o valor total)

total = float(input("Digite o valor: "))
desconto_10 = total - (0.10 * total)
parcelado = total / 3
comissao_desconto = desconto_10 * 0.05
comissao_parcela =total * 0.05
print('''
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
O valor total do produto:                               R${0:.2f}
Com desconto de 10% =                                   R${1:.2f}
Parcelando 3x sem juros =                               R${2:.2f}
Comissão a vista com desconto de 10% =                  R${3:.2f}
Comissão parcelado 5% =                                 R${4:.2f} 
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
'''.format(total,desconto_10,parcelado,comissao_desconto,comissao_parcela))
