"""
2.Faça uma função que receba a data atual (dia, mês e ano em inteiro) e exiba-a
na tela no formato textual por extenso. Exemplo: Data: 01/01/2000, Imprimir:
1 de janeiro de 2000.
"""

def data(dia,mes,ano):
  print()
  if mes == 1:
    if (dia >= 1) and (dia <= 31):
      print(f"{dia} de janeiro de {ano}")
    else:
      print('Data inválida')
  elif mes == 2:
    if (ano % 400 == 0) or ((ano % 4 == 0) and not (ano % 100 == 0)):
      if (dia >= 1) and (dia <= 29):
        print(f'{dia} de fevereiro de {ano}')
      else:
        print('Data inválida')
    else:
      if (dia >= 1) and (dia <= 28):
        print(f"{dia} de fevereiro de {ano}")
      else:
        print('Data inválida')
  elif mes == 3:
    if (dia >= 1) and (dia <= 31):
      print(f"{dia} de março de {ano}")
    else:
      print('Data inválida')
  elif mes == 4:
    if (dia >= 1) and (dia <= 30):
      print(f"{dia} de abril de {ano}")
    else:
      print('Data inválida')
  elif mes == 5:
    if (dia >= 1) and (dia <= 31):
      print(f"{dia} de Maio de {ano}")
    else:
      print('Data inválida')
  elif mes == 6:
    if (dia >= 1) and (dia <= 30):
      print(f"{dia} de junho de {ano}")
    else:
      print('Data inválida')
  elif mes == 7:
    if (dia >= 1) and (dia <= 31):
      print(f"{dia} de julho de {ano}")
    else:
      print('Data inválida')
  elif mes == 8:
    if (dia >= 1) and (dia <= 31):
      print(f"{dia} de agosto de {ano}")
    else:
      print('Data inválida')
  elif mes == 9:
    if (dia >= 1) and (dia <= 30):
      print(f"{dia} de setembro de {ano}")
    else:
      print('Data inválida')
  elif mes == 10:
    if (dia >= 1) and (dia <= 31):
      print(f"{dia} de outubro de {ano}")
    else:
      print('Data inválida')
  elif mes == 11:
    if (dia >= 1) and (dia <= 30):
      print(f"{dia} de novembro de {ano}")
    else:
      print('Data inválida')
  elif mes == 12:
    if (dia >= 1) and (dia <= 31):
      print(f"{dia} de dezembro de {ano}")
    else:
      print('Data inválida')
  
dia = int(input("Digite o dia: "))
mes = int(input("Digite o mês: "))
ano = int(input("Digite o ano: "))

data(dia, mes, ano)
