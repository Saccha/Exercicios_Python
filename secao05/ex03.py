'''
3. Leia um número real. Se o número for positivo imprima a raiz quadrada. Do contrário,
imprima o número ao quadrado.
'''

x = int(input("Digite o valor de x: "))

if ( x > 0 ):
  raiz = int(x ** (1/2))
  print(f"O número {x} é positivo e sua raiz quadrada é {raiz}")
else:
  quad = x ** 2
  print(f"O número {x} é negativo e este número ao quadrado é {quad}")  
