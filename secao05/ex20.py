"""
20. Dados três valores, A, B, C, verificar se eles podem ser valores dos lados de um triângulo
e, se forem, se é um triângulo ESCALENO, EQUILÁTERO ou ISÓSCELE, considerando os seguin-
tes conceitos:
- O comprimento de cada lado de um triângulo é menor do que a soma dos outros dois lados;
- Chama-se equilátero o triângulo que tem três lados iguais;
- Denominam-se isósceles o triângulo que tem o comprimento de dois lados iguais;
- Recebe o nome de escaleno o triângulo que tem os três lados diferentes.
"""
a = float(input('Insira o valor A: '))
b = float(input('Insira o valor B: '))
c = float(input('Insira o valor C: '))

if (a < b + c and b < a + c and c < a + b):
  if (a == b == c):
    print("Esse triângulo é Equilátero.")

  elif (a == b != c or b == c != b or a == c != b):
    print('Esse triângulo é Isóscele.')

  elif a != b != c:
    print('Esse triângulo é Escaleno.')

else:
    print('Não é possível formar um triângulo com esses valores.')
