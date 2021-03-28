"""
22.Crie uma função que receba parâmetro um valor inteiro e gere como
saída n linhas com pontos de exclamação, conforme o exemplo abaixo (para n = 5):
    !
    !!
    !!!
    !!!!
    !!!!!
"""
def exclamacao(linhas):
    for i in range(1, linhas+1):
        print('!'*i)
    return

exclamacao(5)
