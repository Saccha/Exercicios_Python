""" 17. Leia um valor de comprimento em centímetros e apresente-o convertido em polegadas.
A fórmula de conversão é: P = C/2,54,sendo C o comprimento em centímetros e P o comprimento 
em polegadas."""

c = float(input("Digite um valor do comprimento em centimetros: "))
p = c/2.54
print("%.4f" % p)
