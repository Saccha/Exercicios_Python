"""
4. Faça um programa que leia um número e, caso ele seja positivo, calcule e mostre:
- O número digitado ao quadrado;
- A raiz quadrada do número digitado.
"""

num = int(input("Digite o valor desse número: "))

if num > 0:
    expoente = num ** 2
    raiz = int(num ** (1/2))
    print(f"O quadrado do número digitado será {expoente} e sua raiz quadrada será {raiz}.")
else:
    print("Número inválido.")
