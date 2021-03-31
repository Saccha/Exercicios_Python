'''
42.Faça uma função que receba um vetor de reais e retorne a média dele.
'''
def media(*args):
  return sum(args)/len(args)
print(media(6,9))
