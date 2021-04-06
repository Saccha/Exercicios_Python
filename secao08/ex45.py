'''
45.Faça uma função que calcule o desvio padrão de um vetor v contendo n números.
'''
def desvio_padrao(args):
    n = len(args)
    m = sum(args) / len(args)
    dist = 0
    for i in args:
        dist += (i - m) ** 2
    return (dist / n) ** 0.5
print(f"\nDesvio padrão: {desvio_padrao([22, 4000, 98348, 2131, 242321, 213456, 9768.43, 345.45])}")
