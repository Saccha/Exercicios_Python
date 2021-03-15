"""
39. Uma empresa decide dar um aumento aos seus funcionários de acordo com uma tabela
que considera o salário atual e o tempo de serviço de cada funcionário. Os funcionários
com menor salário terão um aumento proporcionalmente maior do que os funcionários
com um salário maior, e conforme o tempo de serviço na empresa, cada funcionário irá
receber um bônus adicional de salário. Faça um programa que leia:
- O valor do salário atual do funcionário;
- O tempo de serviço desse funcionário na empresa (número de anos de trabalho na
empresa).
Use as tabelas abaixo para calcular o salário reajustado deste funcionário e imprima o
valor do salário final reajustado, ou uma mensagem caso o funcionário não tenha direito
a nenhum aumento.
** TABELA NA FOLHA DE EXERCICIOS DA SEÇÃO 5 **
"""
salario = float(input("Digite o valor do salário R$ "))
tempo_de_servico = int(input("Digite o tempo de serviço em anos: "))

# Até 500,00
if salario <= 500:
    reajuste = salario * (125 / 100)
    # Abaixo de 1 ano
    if tempo_de_servico < 1:
        print(f"O salário passará a ser R${reajuste} e não receberá bônus.")
        print(f"TOTAL: R${reajuste}")
    # De 1 a 3 anos
    elif 1 <= tempo_de_servico <= 3:
        bonus = 100
        print(f"O salário passará a ser R${reajuste} + R${bonus} de bônus.")
        print(f"TOTAL: R${reajuste + bonus}")
    # De 4 a 6 anos
    elif 4 <= tempo_de_servico <= 6:
        bonus = 200
        print(f"O salário passará a ser R${reajuste} + R${bonus} de bônus.")
        print(f"TOTAL: R${reajuste + bonus}")
    # De 7 a 10 anos
    elif 7 <= tempo_de_servico <= 10:
        bonus = 300
        print(f"O salário passará a ser R${reajuste} + R${bonus} de bônus.")
        print(f"TOTAL: R${reajuste + bonus}")
    # Mais de 10 anos
    elif tempo_de_servico > 10:
        bonus = 500
        print(f"O salário passará a ser R${reajuste} + R${bonus} de bônus.")
        print(f"TOTAL: R${reajuste + bonus}")

# De 500 a 1000
elif 500 < salario <= 1000:
    reajuste = salario * (120 / 100)
    # Abaixo de 1 ano
    if tempo_de_servico < 1:
        print(f"O salário passará a ser R${reajuste} e não receberá bônus.")
        print(f"TOTAL: R${reajuste}")
    # De 1 a 3 anos
    elif 1 <= tempo_de_servico <= 3:
        bonus = 100
        print(f"O salário passará a ser R${reajuste} + R${bonus} de bônus.")
        print(f"TOTAL: R${reajuste + bonus}")
    # De 4 a 6 anos
    elif 4 <= tempo_de_servico <= 6:
        bonus = 200
        print(f"O salário passará a ser R${reajuste} + R${bonus} de bônus.")
        print(f"TOTAL: R${reajuste + bonus}")
    # De 7 a 10 anos
    elif 7 <= tempo_de_servico <= 10:
        bonus = 300
        print(f"O salário passará a ser R${reajuste} + R${bonus} de bônus.")
        print(f"TOTAL: R${reajuste + bonus}")
    # Mais de 10 anos
    elif tempo_de_servico > 10:
        bonus = 500
        print(f"O salário passará a ser R${reajuste} + R${bonus} de bônus.")
        print(f"TOTAL: R${reajuste + bonus}")

# De 1000 a 1500
elif 1000 < salario <= 1500:
    reajuste = salario * (115 / 100)
    # Abaixo de 1 ano
    if tempo_de_servico < 1:
        print(f"O salário passará a ser R${reajuste} e não receberá bônus.")
        print(f"TOTAL: R${reajuste}")
    # De 1 a 3 anos
    elif 1 <= tempo_de_servico <= 3:
        bonus = 100
        print(f"O salário passará a ser R${reajuste} + R${bonus} de bônus.")
        print(f"TOTAL: R${reajuste + bonus}")
    # De 4 a 6 anos
    elif 4 <= tempo_de_servico <= 6:
        bonus = 200
        print(f"O salário passará a ser R${reajuste} + R${bonus} de bônus.")
        print(f"TOTAL: R${reajuste + bonus}")
    # De 7 a 10 anos
    elif 7 <= tempo_de_servico <= 10:
        bonus = 300
        print(f"O salário passará a ser R${reajuste} + R${bonus} de bônus.")
        print(f"TOTAL: R${reajuste + bonus}")
    # Mais de 10 anos
    elif tempo_de_servico > 10:
        bonus = 500
        print(f"O salário passará a ser R${reajuste} + R${bonus} de bônus.")
        print(f"TOTAL: R${reajuste + bonus}")

# De 1500 a 2000
elif 1500 < salario <= 2000:
    reajuste = salario * (110 / 100)
    # Abaixo de 1 ano
    if tempo_de_servico < 1:
        print(f"O salário passará a ser R${reajuste} e não receberá bônus.")
        print(f"TOTAL: R${reajuste}")
    # De 1 a 3 anos
    elif 1 <= tempo_de_servico <= 3:
        bonus = 100
        print(f"O salário passará a ser R${reajuste} + R${bonus} de bônus.")
        print(f"TOTAL: R${reajuste + bonus}")
    # De 4 a 6 anos
    elif 4 <= tempo_de_servico <= 6:
        bonus = 200
        print(f"O salário passará a ser R${reajuste} + R${bonus} de bônus.")
        print(f"TOTAL: R${reajuste + bonus}")
    # De 7 a 10 anos
    elif 7 <= tempo_de_servico <= 10:
        bonus = 300
        print(f"O salário passará a ser R${reajuste} + R${bonus} de bônus.")
        print(f"TOTAL: R${reajuste + bonus}")
    # Mais de 10 anos
    elif tempo_de_servico > 10:
        bonus = 500
        print(f"O salário passará a ser R${reajuste} + R${bonus} de bônus.")
        print(f"TOTAL: R${reajuste + bonus}")

# Acima de 2000
elif salario > 2000:
    reajuste = salario
    # Abaixo de 1 ano
    if tempo_de_servico < 1:
        print(f"O salário passará a ser R${reajuste} e não receberá bônus.")
        print(f"TOTAL: R${reajuste}")
    # De 1 a 3 anos
    elif 1 <= tempo_de_servico <= 3:
        bonus = 100
        print(f"O salário passará a ser R${reajuste} + R${bonus} de bônus.")
        print(f"TOTAL: R${reajuste + bonus}")
    # De 4 a 6 anos
    elif 4 <= tempo_de_servico <= 6:
        bonus = 200
        print(f"O salário passará a ser R${reajuste} + R${bonus} de bônus.")
        print(f"TOTAL: R${reajuste + bonus}")
    # De 7 a 10 anos
    elif 7 <= tempo_de_servico <= 10:
        bonus = 300
        print(f"O salário passará a ser R${reajuste} + R${bonus} de bônus.")
        print(f"TOTAL: R${reajuste + bonus}")
    # Mais de 10 anos
    elif tempo_de_servico > 10:
        bonus = 500
        print(f"O salário passará a ser R${reajuste} + R${bonus} de bônus.")
        print(f"TOTAL: R${reajuste + bonus}")
