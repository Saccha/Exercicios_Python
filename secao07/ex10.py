"""
10.Faça um programa para ler a nota da prova de 15 alunos.txt e armazene num vetor,
calcule e imprima a média geral.
"""

lista = []
for i in range(15):
  lista.append(float(input(f"Digite a nota do {i + 1}° aluno: ")))

print('n\A média geral dos alunos.txt: %.1f' % (sum(lista) / len(lista)))
