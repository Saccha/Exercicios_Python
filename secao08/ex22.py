"""
22.Crie uma função que receba parâmetro um valor inteiro e gere como
saída n linhas com pontos de exclamação, conforme o exemplo abaixo (para n = 5):
    !
    !!
    !!!
    !!!!
    !!!!!
"""
def pontos(num):
  print()
  if (num > 0) and (num // 1 == num):
    for i in range(1 , num+1):
      print("!" * i)
  else:
    print("Número inválido")
num = int(input("Digite um número: "))
pontos(num)
