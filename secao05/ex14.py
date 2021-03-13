"""
14. A nota de um estudante é calculada a partir de três notas atribuídas entre o intervalo
de 0 até 10, respectivamente, a um trabalho de laboratório, a uma avaliação semestral
e a um exame final. A média das três notas mencionadas anteriormente obedece aos
pesos: TRABALHO DE LABORATÓRIO: 2; AVALIAÇÃO SEMESTRAL: 3; EXAME FINAL: 5. De acordo
com o resultado, mostre na tela se o aluno está reprovado (média entre 0 e 2,9), de
recuperação (entre 3 e 4,9) ou se foi aprovado. Faça todas as verificações necessárias.
"""

nota1 = float(input("Digite a nota do Trabalho de Laboratório: "))
nota2 = float(input("Digite a nota da Avaliação Semestral: "))
nota3 = float(input("Digite a nota do Exame Final: "))

media_final = ((nota1 * 2) + (nota2 * 3) + (nota3 * 5)) / (2 + 3 + 5)

print(media_final)

if 0 <= media_final <= 2.9:
    print("Aluno REPROVADO.")
elif 3 <= media_final <= 4.9:
    print("Aluno de RECUPERAÇÃO.")
else:
    print("Aluno APROVADO.")
