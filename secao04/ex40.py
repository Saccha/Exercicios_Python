#40. Uma empresa contrata um encanador a R$ 30,00 por dia. Faça um programa que solicite
# o número de dias trabalhandos pelo encanador e imprima a quantia líquida que deverá
# ser paga, sabendo-se que são descontados 8% para impostos de renda.


dias = int(input('Digite os dias trabalhador: '))
valor_bruto = 30 * dias
impostos = 0.08 *valor_bruto
pagamento = valor_bruto - impostos
print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
print()
print('O pagamento total é de R$ {0:.2f}:'.format(pagamento))
print('''
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
dias trabalhado =         {0}
valor bruto =        R$ {1:.2f}
imposto              R$ {2:.2f}
pagamento =          R$ {3:.2f}
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
'''.format(dias,valor_bruto,impostos,pagamento))
