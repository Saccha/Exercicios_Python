#28.  Faça a leitura de três valores e apresente como resultado a soma dos quadrados dos 
# três valores lidos.

n1 = int(input('Digite o 1º número: '))
n2 = int(input('Digite o 2º número: '))
n3 = int(input('Digite o 3º número: '))
soma = (n1 ** 2)+(n2 ** 2)+(n3 ** 2)
print('A soma dos quadrados dos três valores({0},{1},{2}) é {3}.'.format(n1,n2,n3,soma))
