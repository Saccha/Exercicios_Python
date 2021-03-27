"""
6.Faça uma função que receba 3 números inteiros como parâmetro,
representando horas, minutos e segundos, e os converta em segundos
"""

def tempo(horas,minutos,segundos):
  if horas // 1 == horas:
    if minutos // 1 == minutos:
      if segundos // 1 == segundos:
        convertido = horas * 60 * 60
        convertido += minutos * 60
        convertido += segundos
        return convertido
horas = int(input("Digite as horas: "))
minutos = int(input("Digite os minutos: "))
segundos = int(input("Digite os segundos: "))
print(f'\nConvertido em segundos: {tempo(horas,minutos,segundos)}')
