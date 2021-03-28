"""
10.Faça uma função que receba dois números e retorne qual deles é o maior.
    Função que recebe dois números e retorna o maior número
    :param numero1: recebe um valor
    :param numero2: recebe um valor
    :return: retorna o maior número ('numero1' ou 'numero2')
"""
def maior(num1,num2):
    # Achando o maior número
    maior = num1
    if (num2 > maior):
        maior = num2
    return maior

num1 = int(input('Primeiro numero: '))
num2  = int(input('Segundo numero : '))
print(f"\nO maior número: {maior(num1, num2)}")
