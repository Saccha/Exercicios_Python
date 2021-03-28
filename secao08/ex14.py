"""
14) Faça uma função que receba a distância em Km e a quantidade de litros de gasolina
consumidos por um carro em um percurso, calcule o consumo em km/l e escreva uma mensagem
de acordo com a tabela abaixo:
    | CONSUMO    | (km/l)  | MENSAGEM
    | menor que  |   8     | Venda o carro!
    | entre      | 8 e 12  | Econômico
    | maior que  |  12     | Super econômico!
"""
def consumo_km(distancia,gasolina):
  consumo = distancia / gasolina
  if consumo < 0:
    print('Vendo o carro!')
  elif (consumo >= 8) and (consumo <= 14):
    print('Econômico!')
  elif (consumo > 12):
    print('Super econômico!')
distancia = float(input("Digite a distnância em km: "))
gasolina = float(input("Digite o consumo da gasolina consumida pelo carro: ")) 
consumo_km(distancia,gasolina)
