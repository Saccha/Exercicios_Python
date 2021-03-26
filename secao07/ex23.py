"""
23.Ler dois conjuntos de números reais, armazenando-os em vetores
e calcular o produto escalar entre eles. Os conjuntos têm 5 elementos
cada. Imprimir os dois conjuntos e o produto escalar, sendo que o produto
escalar é dado por: x1 * y1 + x2 * y2 + ... + xn * yn
"""

lista1 = []
lista2 = []
for i in range(5):
  lista1.append(float(input("Digite um valor para o primeiro vetor: ")))

for i in range(5):
  lsita2.append(float(input("Digite um valor para o segundo vetor: ")))

print(f'\nPrimeir vetor: {lista1}')
print(f'\nSegundo vetor: {lista2}')

produto_escalar = 0.0
for i in range(5):
  produto_escalar += (lista1[i] * (i+1)) * (lista2[i] * (i+1))
print(f'Produto escalar dos dois conjuntos : {produto_escalar}')
