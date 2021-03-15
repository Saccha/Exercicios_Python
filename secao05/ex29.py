"""
29. Faça uma prova de matématica para crianças que estão aprendendo a somar números
inteiros menores do que 100. Escolha números aleatórios entre 1 e 100, e mostre na
tela a pergunta: Qual é a soma de A e B, onde A e B são números aleatórios. Peça a
resposta. Faça cinco perguntas ao aluno, e mostre ára ele as perguntas e as respostas
corretas, além de quantas vezes o aluno acertou.
"""
import random

a1 = random.randint(1, 100)
a2 = random.randint(1, 100)

contagem = 0
soma = int(input(f"Qual a soma de {a1} e {a2}? "))
resultado = a1 + a2

if soma == resultado:
    print("Acertou.")
    contagem = contagem + 1
else:
    print(f"Errado. A resposta correta é {resultado}!")

# -------------------------------------------------------------

b1 = random.randint(1, 100)
b2 = random.randint(1, 100)

soma = int(input(f"Qual a soma de {b1} e {b2}? "))
resultado = b1 + b2

if soma == resultado:
    print("Acertou.")
    contagem = contagem + 1
else:
    print(f"Errado. A resposta correta é {resultado}!")

# -------------------------------------------------------------

c1 = random.randint(1, 100)
c2 = random.randint(1, 100)

soma = int(input(f"Qual a soma de {c1} e {c2}? "))
resultado = c1 + c2

if soma == resultado:
    print("Acertou.")
    contagem = contagem + 1
else:
    print(f"Errado. a resposta correta é {resultado}")

# -------------------------------------------------------------

d1 = random.randint(1, 100)
d2 = random.randint(1, 100)

soma = int(input(f"Qual a soma de {d1} e {d2}? "))
resultado = d1 + d2

if soma == resultado:
    print("Acertou.")
    contagem = contagem + 1
else:
    print(f"Errado. A resposta certa é {resultado}")

# ------------------------------------------------------------

e1 = random.randint(1, 100)
e2 = random.randint(1, 100)

soma = int(input(f"Qual a soma de {e1} e {e2}? "))
resultado = e1 + e2

if soma == resultado:
    print("Acertou.")
    contagem = contagem + 1
else:
    print(f"Errado. A resposta correta é {resultado}")

if contagem == 5:
    print("Parabéns, acertou tudo.")
elif contagem >= 3:
    print("Dá pra melhorar")
elif 1 <= contagem < 3:
    print("Tá péssimo.")
elif contagem == 0:
    print("Você é um lixo de ser humano.")
