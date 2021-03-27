"""
7.Faça uma função que receba uma temperatura en graus Celsius e retorne-a
convertida em graus Fahrenheit. A fórmula de conversão é: F = C * (9.0/5.0) + 32.0,
sendo F a temperatura em Fahrenheit e C a temperatura em Celsius.
"""
def converter(celsius):
  return celsius * (9.0/5.0) + 32.0
celsius = float(input("Digite a temperatura em graus celsius: "))
print(f"\nTemperatura em graus Fahrenheit: {converter(celsius)}°F")
