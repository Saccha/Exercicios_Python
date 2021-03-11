#41. Faça um programa que leia o valor da hora de trabalho (em reais) e número de horas
# trabalhadas no mês. Imprima o valor a ser pago ao funcionário. adicionando 10% sobre
# o valor calculado.
 

hora_valor = int(input('Digite quanto vale a hora de trabalho em reais:  '))
horas_trabalhada = int(input('Digite quantas horas foram trabalhada no mês: '))
pagamento = hora_valor*horas_trabalhada
pagamento_10 = (0.10*pagamento)+pagamento
print('Pagamento = R${0:.2f}'.format(pagamento_10))
