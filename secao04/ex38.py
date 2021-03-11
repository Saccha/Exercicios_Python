#38. Leia o salário de um funcionário. Calcule e imprima o valor do novo salário, sabendo que 
# ele recebeu um aumento de 25%.


salario = float(input('Digite o valor do salario: '))
aumento = 0.25*salario
salario_25 = salario + aumento
print('O Salário é de R${1} com um aumento de 25% teve um aumento de R${0} totalizando R${2}.'.format(aumento,salario,salario_25))
