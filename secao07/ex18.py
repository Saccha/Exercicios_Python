"""
18.Faça um programa que leia um vetor de 10 números. Leia um
número x. Conte os múltiplos de um número inteiro x num vetor
e mostre-os na tela.
"""
#Montar lista
lista = []
for i in range(10):
  lista.append(int(input("Digite um número: ")))
x = int(input("\nDigite um valor de x: "))

#Montar a lista com multiplos que o susuário desejar digitar
multiplo = []
for i in range(10):
  multiplo.append(x * lista[i])
print(f"\nOs múltiplos de {x} de acordo com os valores digitados:")
print(*multiplo, sep=', ')
