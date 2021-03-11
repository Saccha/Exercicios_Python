#37. Faça um programa que leia o valor de um produto e imprima o valor com desconto,tendo
# em vista que o desconto foi de 12%.

valor = float(input('Digite o valor do produto para saber o desconto: '))
desconto_12 = 0.12*valor
valor_com_desconto = valor - desconto_12 
print('O produto de R${0} com desconto de 12%(R${2}) tem o valor total de  R${1}'.format(valor,valor_com_desconto,desconto_12)) 
