""" 6. Leia uma temperatura em graus Celsius e apresente-a convertida em gruas Fahrenheit. A fórmula de conversão é:  
F = C*(9.0/5.0)+32.0, sendo F a temperatura em Fahrenheit e C a temperatura em gruas Celsius"""
# 6
c = float(input("Digite o valor: "))
f = c * (9.0 / 5.0) + 32.0
print("%.1f" % f)
