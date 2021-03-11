#30. Leia um valor em real e a cotação do dólar. Em seguida, emprima o valor correspondente
# em dólares.

real = float(input('Digite em rela para converter em dólar: '))
valor = float(input('Digite o valor do dólar atual: '))
dolar = (1/valor)*real
print('{0} real = {2:.2f} dólar valor do dólar({1})'.format(real,valor,dolar))
