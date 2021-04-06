'''
44.Faça uma função que receba como parâmetro um vetor X de 30 elementos inteiros e retorne, também por parâmetro, 
dois vetores A e B. O vetor A deve conter os elementos pares de X e o vetor B, os elementos ímpares.
'''

def par_impar(*args):
    a = []
    b = []
    for i in args:
        if i%2 == 0:
            a.append(i)
        elif i%2 != 0:
            b.append(i)
    return f'Pares: {a}\nÍmpares: {b}'

print(par_impar(1,2,3,15,20,30,68,45,32,45,67,14,100))
