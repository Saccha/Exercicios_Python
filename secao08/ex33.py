"""
33.Faça uma função que receba um número N e retorne a soma dos algarismos de N!.
"""
def soma(num):
    fat = 1
    sum = 0
    for i in range(1, num+1):
        fat *= i
    fat = str(fat)
    for i in fat:
        i = int(i)
        sum += i
    return f'A soma dos algarismos de {fat} é {sum}'
print(soma(10))
