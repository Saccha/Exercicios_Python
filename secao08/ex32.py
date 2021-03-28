'''
32.Faça um função chamada 'simplifica' que recebe como parâmetro o numerador e o denominador de uma fração. Esta
função deve simplificar a fração recebida dividindo o numerador e o denominador pelo maior fator possível. 
'''
def simplifica(num,deno):
  tupla = (num,deno)
  limite = max(tupla)
  for i in range(1 , limite + 1):
    if num % i == 0 and deno % i == 0:
      fator = i
  return f'A fração {num}/{deno} equivale a {int(num/fator)}/{int(deno/fator)}.'

num = int(input("Digite um numerador: "))
deno = int(input("Digite um denominador: "))
simplifica(num,deno)
