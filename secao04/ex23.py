#23. Leia uma valor de comprimento em metros e apresente-o convertido em jardas. A fórmula 
# de conversão é: J = M/0,91 ,sendo J o comprimento em jardas e M o comprimento em metros

m = float(input("Digite em metros para converter em jardas: "))
j = m/0.91
print('{0} metros = {1:.2f} jardas '.format(m,j))
