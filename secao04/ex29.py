#29.  Leia quatro notas, calcule a média aritmética e imprima o resultado.

nota1 = float(input('Digite o valor da primeira nota: '))
nota2 = float(input('Digite o valor da segunda nota: '))
nota3 = float(input('Digite o valor da terceira nota: '))
nota4 = float(input('Digite o valor da quarta nota: '))

media = (nota1 + nota2 + nota3 + nota4)/4
print('Suas notas foram ({0},{1},{2},{3}) e a media é {4}'.format(nota1,nota2,nota3,nota4,media))
