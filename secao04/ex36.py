#36. Leia a altura e o raio de um cilindro circular e imprima o volume do cilindro. O volume
# de um cilindro círcular é calculado por meio da seguinte fórmula: V = π * raio²* altura,
#  onde π = 3.141592

A = float(input('Digite a altura do cilindro circular: '))
R = float(input('Digite o raio do cilindro circular: '))
V = 3.14*R**2*A
print('O volume do cilindro circular é de {0:.2f}'.format(V))
