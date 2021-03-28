'''
25.Faça um função que receba um inteiro N como parâmetro, calcule e retorne o resultado da seguinte série:
S = 2/4 + 5/5 + 10/6 + ... + (N² + 1)/(N + 3).
'''
def calcula(num):
  soma = 0
  for i in range(1, num+1):
    soma += (i**2+1)/(i+3)
  return round(soma,2)
print(calcula(20))
