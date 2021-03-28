"""
9.Faça uma função que receba a altura e o raio de um cilindro circular e
retorne o volume do cilindro. O volume de um cilindro circular é calculado por meio
da seguinte fórmula: V = r * (raio ** 2) * altura, onde r = 3.141592
    Função que recebe a altura e o raio de um cilindro e retorna o volume do mesmo
    :param altura: recebe a altura do cilindro
    :param raio: recebe o raio do cilindro
    :return: retorna o valor do volume do cilindro
"""
def cilindro(altura,raio):
  pi = 3.141592
  return pi * (raio ** 2) * altura
altura = float(input("Digite a altura do cilindro: "))
raio = float(input("Digite o raio do cilindro: "))
print(f"\nO volume do cilindro: {cilindro(altura, raio)}")
