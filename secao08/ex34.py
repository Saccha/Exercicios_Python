'''
34.Faça uma função não-recursiva que receba um número inteiro positivo ímpar N e retorne o fatorial duplo desse
número. O fatorial duplo é definido como o produto de todos os números naturais ímpares de 1 até algum 
número natural ímpar N.
'''
def duplo(num):
  if (num % 2 == 0):
    return "Número inválido"
  prod = 1
  for i in range(1,num+1,2):
    prod *= i
  return prod

num = int(input("Digite um número: "))
print(f"\nFatorial duplo de {num}: {duplo(num)}")
