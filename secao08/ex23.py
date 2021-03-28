'''
23.Escreva uma função que gere um triângulo lateral de altura 2*n-1 e largura n.
'''
def triangulo(x):
  for i in range(1, x+1):
    print("*" * i)
  for i in range(x-1,0,-1):
    print("*" * i)
  return
triangulo(5)
