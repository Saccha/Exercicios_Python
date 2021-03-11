#27.  Leia um valor de área em hectares e apresente-o convertido em metros quadrados m².
# A fórmula de conversão é: M = H * 10000, sendo M a área em metros quadrados e H 
# a área em hectares.

h = float(input("Digite um hectare para converter em metros quadrados: "))
m = h * 10000
print('{0} hectare = {1} metros quadrados'.format(h,m))
