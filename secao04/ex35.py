#35. Sejam a e b os catetos de um triângulo, onde a hipotenusa é obtida pela equação:
# hipotenusa = ²(a²,b²). Faça um programa que receba os valores de a e b e c calcule
# o valor da hipotenusa através da equação. Imprima o resuldado dessa operação.


a = float(input('Digite o valor de cateto oposto [a]: '))
b = float(input('Digite o valor de cateto adijacente [b]: '))
c = (a**2+ b**2)**(1/2)
print('O valor da hipotenusa é {0:.2}'.format(c))
