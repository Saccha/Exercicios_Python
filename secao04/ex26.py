#26. Leia um valor de área em metros quadrados m² e apresente-o convertido em hectare.
# A fórmula de conversão é: H = M * 0,0001, sendo M a área em metros quadrados e H
# área em hectares. 

m = float(input("Digite a área em metros quadrados m² para converter em hectare: "))
h = m * 0.0001
print('{0} metros quadrados = {1} hectare'.format(m,h))
