"""
34. Leia a nota e o número de faltas de um aluno, escreva seu conceito. De acordo com a
tabela abaixo, quando o aluno tem mais de 20 faltas ocorre uma redução de conceito.
** TABELA NA FOLHA DE EXERCICIOS DA SEÇÃO 5 **
"""
nota = float(input("Digite a nota do aluno: "))
faltas = int(input("Digite o número de faltas: "))

if faltas <= 20:
    if 9 <= nota <= 10:
        print("Conceito A")
    elif 7.5 <= nota <= 8.9:
        print("Conceito B")
    elif 5 <= nota <= 7.4:
        print("Conceito C")
    elif 4 <= nota <= 4.9:
        print("Conceito D")
    elif 0 <= nota <= 3.9:
        print("Conceito E")
    else:
        print("Nota inválida.")

elif faltas > 20:
    if 9 <= nota <= 10:
        print("Conceito B")
    elif 7.5 <= nota <= 8.9:
        print("Conceito C")
    elif 5 <= nota <= 7.4:
        print("Conceito D")
    elif 4 <= nota <= 4.9:
        print("Conceito E")
    elif 0 <= nota <= 3.9:
        print("Conceito E")
    else:
        print("Nota inválida.")
