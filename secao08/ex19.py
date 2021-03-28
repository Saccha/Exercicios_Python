"""
19.Faça uma função que retorne o maior fator primo de um número.
"""
def fator(num):
  if num // 1 == num:
    divisores = int(num)
    maior = 0
    for i in range(1, divisores+1):
      cont = 0
      for j in range(1,i+1):
        if i % j == 0:
          cont += 1
      if cont == 2:
        if divisores % i == 0:
          if i > maior:
            maior = i
          divisores /= i
      elif cont == 1:
        if i > maior:
          maior = i
    return maior
num = float(input("Digite um número: "))
print(f"\nMaior fator primo de {num}: {fator(num)}")
