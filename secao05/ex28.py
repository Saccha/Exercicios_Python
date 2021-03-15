"""
28. Faça um programa que leia três números positivos e efetue o cálculo de uma das
seguintes médias de acordo com um valor numérico digitado pelo usuário:
A) GEOMÉTRICA
B) PONDERADA
C) HARMÔNICA
D) ARITMÉTICA
"""

x = int(input("Digite o valor de x: "))
y = int(input("Digite o valor de y: "))
z = int(input("Digite o valor de z: "))

print("Tipos de média.")
print("1> GEOMÉTRICA.")
print("2> PONDERADA.")
print("3> HARMÔNICA.")
print("4> ARTIMÉTICA.")

tipo_media = int(input("Digite o tipo de média correspondente: "))

if tipo_media == 1:
  print("Média Geométrica")
  result = ( x * y * z) ** (1/3)
  print(f'O resultado é {result}')

elif tipo_media == 2:
  print("Média Ponderada")
  result = (x + (2 * y) + (3 * z)) / 6
  print(f'O resultado é {result}')

elif tipo_media == 3:
  print("Média Harmônica")
  result = 1 / ((1 / x) + (1 / y) + (1 / z))
  print(f'O resultado é {result}')

elif tipo_media == 4:
    print("Média Aritmética.")
    resultado = (x + y + z) / 3
    print(f"O resultado é {resultado}")

else:
    print("Digite uma opção válida.")
