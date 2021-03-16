"""
8. Escreva um programa que leia 10 números e escreva o menor valor lido e o maior valor lido
"""
maior = 0
menor = 0
for i in range(1,11):
  valor = int(input("Digite o {}° número: ".format(i)))
  if menor == 0 and maior == 0:
    maior = valor
    menor = valor
  elif maior <= menor:
    maior = valor
  elif menor >= maior:
    menor = valor

print(f'Maior número {maior}')
print(f'Menor número {menor}')
