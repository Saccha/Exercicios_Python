'''
46.Crie um programa contendo as seguintes funções que recebem um vetor V de números reais como parâmetro:
- Impressão normal do vetor
- Impressão inversa
- Função que retorna a média aritmética dos elementos do vetor
'''
import random

tam = int(input("Digite o tamanho que deseja: "))
vetor = []
i = 0

while i < tam:
    num = random.randrange(0, 201)
    vetor.append(num)
    i += 1

def impressao(*args):
    print(vetor)
    return

def impressao_reversa(vetor):
    vetor.reverse()
    print(vetor)
    return

def media(vetor):
    media = sum(vetor)/len(vetor)
    return media

impressao(vetor)
impressao_reversa(vetor)
print(media(vetor))
