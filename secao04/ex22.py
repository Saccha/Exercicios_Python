#22. Leia um valor de comprimento em jardas e apresente-o convertido em metros. A fórmula 
# de conversão é: M = 0,91 * J, sendo J o comprimento em jardas e M o comprimento em 
# metros. 

j = float(input("Digite o comprimento em jardas para converter em metros: "))
m = 0.91 * j
print('{0} jardas = {1} metros'.format(j,m))
