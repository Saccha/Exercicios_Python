#21. Leia um valor de massa em libras e apresente-o convertido em quilogramas. A fórmula
# de conversão é; K = L * 0,45 , sendo K a massa em quilogramas e L a massa em libras.

l = float(input("Digite o valor de massa em libras para converte em quilogramas: "))
k = l * 0.45
print('{0} libras = {1} quilograma '.format(l,k))
