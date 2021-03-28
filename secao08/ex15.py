"""
15) Crie um programa que receba três valores (obrigatoriamente maiores que zero),
representando as medidas dos três lados de um triângulo. Elabore funções para:
(a) Determimnar se eles lados formam um triângulo, sabendo que:
    . O comprimento de cada lado de um triângulo é menor do que a soma dos outros
    dois lados.
(b) Determinar e mostrar o tipo de triângulo, caso as medidas formem um
triângulo. Sendo que:
    . Chama-se equilátero o triângulo que tem três lados iguais.
    . Denominam-se isósceles o triângulo que tem o comprimento
    de dois lados iguais
    . Recebe o nome de escaleno o triângulo que tem os três lados diferentes.
"""
def triangulo(medida1, medida2, medida3):
    if medida1 > 0 and medida2 > 0 and medida3 > 0:
        if medida1 <= (medida2 + medida3):
            if medida2 <= (medida1 + medida3):
                if medida3 <= (medida1 + medida2):
                    return "Os lados formam um triângulo"
        return "Os lados não formam um triângulo"
    return "Os valores são menores que zero"

def tipo_triangulo(medida1, medida2, medida3):
    retorno = triangulo(medida1, medida2, medida3)
    if retorno.lower() == "os lados formam um triângulo":
        if medida1 == medida2 == medida3:
            return "Triângulo equilátero"
        elif ((medida1 == medida2) and (medida2 != medida3)) or ((medida2 == medida3) and (medida3 != medida1)):
            return "Triângulo isósceles"
        return "Triângulo escaleno"
    return "Valores inválidos"
medid1 = float(input("Digite a primeira medida do triângulo: "))
medid2 = float(input("Digite a segunda medida do triângulo: "))
medid3 = float(input("Digite a terceira medida do triângulo: "))
print(f"\n{triangulo(medid1, medid2, medid3)}")
print(f"{tipo_triangulo(medid1, medid2, medid3)}")
