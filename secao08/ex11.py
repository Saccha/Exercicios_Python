"""
11.Escreva uma função que receba um número inteiro maior que zero
e retorne a soma de todos os seus algarismos. Por exemplo,
ao número 251 corresponderá o valor 8 (2 + 5 + 1). Se o número lido
não for maior do que zero, o programa terminará com a mensagem "Número inválido"
Função que recebe três notas de um aluno, uma letra(opcional, que por padrão é 'A', mas que pode ser 'P')
    e retorna uma mensagem informando o valor da média desejada
    :param nota1: Recebe a primeira nota do aluno
    :param nota2: Recebe a segundo nota do aluno
    :param nota3: Recebe a terceira nota do aluno
    :param letra: Recebe uma letra que indicará o calculo que deve ser realizado(opcional)
    :return: Retorna uma mensagem com o valor da média desejada. Se a letra for inválida
    retorna uma mensagem informando que a letra é inválida
"""

def calculo(nota1,nota2,nota3,letra='A'):
  if str(letra).upper() == 'A':
    media = (nota1+nota2+nota3)/3
    return "Média aritmética do aluno: %.1f" % media
  elif str(letra).upper() == 'P':
        media = (nota1 * 5 + nota2 * 3 + nota3 * 2) / 10
        return "Média ponderada do aluno: %.1f" % media

  return 'Letra inválida'


nota1 = float(input("Digite a primeira nota do aluno: "))
nota2 = float(input("Digite a segunda nota do aluno: "))
nota3 = float(input("Digite a terceira nota do aluno: "))

letra = str(input("Digite a letra referente ao calculo: "))

print(f"\n{calculo(nota1, nota2, nota3, letra)}")
