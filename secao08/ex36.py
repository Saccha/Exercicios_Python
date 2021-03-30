'''
36.Faça uma função não-recursiva que receba um número inteiro positivo n e retorne o superfatorial desse número. O 
superfatorial de um número N é definido pelo produto dos N primeiros fatoriais de N.
'''
def superfatorial(num):
  prod = 1
  fat = 1
  for i in range(1,num+1):
    for j in range(1,i+1):
      prod *= j
    fat *= prod
    prod = 1
  return fat

num = int(input("Digite um número: "))
print(f"\nO superfatorial de {num}: {superfatorial(num)}")
