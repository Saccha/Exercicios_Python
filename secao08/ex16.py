'''
16.Faça uma função chamada DesenhaLinha. Ela deve desenhar uma linha na tela usando vários símbolos de igual. A função
deve receber por parâmetro quantos sinais de igual serão mostrados.
'''
def Linha(qtd):
  return print ('=' * qtd)
qtd = int(input("Digite o número: "))
Linha(qtd)
