#32. Leia um número inteiro e imprima a soma do sucessor de seu triplo com o antecessor de
# seu dobro.

n = int(input('Digite um numero inteiro para saber a soma do sucessor e o triplo do antecessor: '))
print('O valor digitado é {0} a soma do seu sucessor é {1} e o triplo do antecessor é {2}'.format(n,n+n+1,(n-1)*3))
