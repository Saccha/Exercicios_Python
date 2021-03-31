'''
40.Faça uma função que receba um vetor de inteiros e retorne quantos valores pares ele possui.
'''
def pares(*args):
  arr = args
  pares = []
  for i in arr:
    if i % 2 == 0:
      pares.append(i)
  return len(pares)
print(pares(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20))
