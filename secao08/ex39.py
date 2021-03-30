'''
39.Faça uma função 'Troque', que receba duas variáveis reais A e B e troca o valor delas.
'''
def troque(a,b):
  tupla = (a,b)
  a = tupla[1]
  b = tupla[0]
  return a,b

a = float(input("Digite o primeiro número: "))
b = float(input("Digite o segundo número: "))
print(f"\n{a} e {b}")
