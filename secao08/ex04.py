"""
4.Faça uma função para verificar se um número é um quadrado perfeito.
Um quadrado perfeito é um número inteiro não negativo que pode ser
expresso como o quadrado de outro número inteiro. Ex: 1, 4, 9...
"""
def quadrado(num):
  if num > 0:
    if (num**0.5) // 1 == num ** 0.5:
      print('\nÉ um quadrado perfeito')
    else:
      print("\nNão é um quadrado perfeito")
  else:
    print("\nO número deve ser positivo")
x = int(input("Digite um número: "))
quadrado(x)
