"""
21) Escreva uma função para determinar a quantidade de números
primos abaixo de N.
"""
def abaixo(num):
  qtd = 0
  if (num > 0) and (num // 1 == num):
    for i in range(1,num):
      cont = 0
      for j in range(1, i + 1):
        if i % j == 0:
          cont += 1
      if cont <= 2:
        qtd += 1
    return qtd
num = int(input("Digite um número: "))
print(f"\nQuantidade de números primos abaixo de {num}: {abaixo(num)}")
