"""
20.Faça um algoritmo que receba um número inteiro positivo n
e calcule o seu fatorial, n!
"""
def fatorial(num):
  if (num > 0) and (num // 1 == num):
    result = 1
    for i in range(1, num+1):
      result *= i
    return result
num = int(input("Digite um número: "))
print(f"\nResultado do fatorial de {num}: {fatorial(num)}")
