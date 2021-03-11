#42. Receba o salário-base de um funcionário. Calcule e imprima o salário a receber, sabendo-
# se que esse funcionário tem uma gratificação de 5% sobre o salário-base. Além disso.
# ele paga 7% de imposto sobre o salário-base.

salario_base = int(input("Digite seu salário: "))
salario_acrescimo = (0.05 * salario_base) + salario_base
imposto = salario_acrescimo - (0.07 * salario_acrescimo)
print('Recebe total = R${0:.2f}'.format(imposto))
