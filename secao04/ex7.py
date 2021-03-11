""" 7. Leia uma temperatura em graus Fahrenheit e apresente-a convertida em gruas Celsius. A fórmula de conversão é:  
C = 5.0*(f-32.0)/9.0, sendo C a temperatura em Celsius e F a temperatura em Fahrenheit"""

f = float(input("Digite o valor de Fahrenheit: "))
c = 5.0 * (f - 32.0) / 9.0
print("%.1f" % c)
