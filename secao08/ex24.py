'''
24.Escreva uma função que gere um triângulo de altura e lados n e base 2*n-1.
'''
def triangulo(x):
  for i in range(1, x+1):
    elemento = "*" * (2*i -1)
    print(f"{elemento:^{x*2}}")
  return
triangulo(10)
