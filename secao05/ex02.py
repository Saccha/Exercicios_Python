'''
2. Leia um número fornecido pelo usuário.Se esse número for positivo, calcule a raiz quadrada do número 
Se o número for negativo, mostre uma mensagem dizendo que o número é inválido
'''

x = int(input("Digite o valor de x: "))

if (x > 0):
  raiz = int(x ** (1/2))
  print(f"O número {x} é POSITIVO e sua RAIZ QUADRADA é {raiz}.")
else:
  print(f"Número inválido")
