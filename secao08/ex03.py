"""
3.Faça uma função para verificar se um número é positivo ou negativo.
Sendo que o valor de retorno será 1 se positivo, -1 se negativo
e 0 se for igual a 0
"""
def num(numero):
  if numero > 0:
    return 1
  elif numero < 0:
    return -1
  return 0
x = int(input("Digite um número: "))
print(f"\n{num(x)}")
