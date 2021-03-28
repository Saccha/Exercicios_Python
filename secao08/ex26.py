'''
26.Faça um algoritmo que receba um número inteiro positivo n e calcule o somatório de 1 até n.
'''
def somatorio(num):
  sum = 0
  for i in range(1,num+1):
    sum += i
  return sum
num = int(input("Digite um número: "))
print(f"\nSomatório de 1 até {num}: {somatorio(num)}")
