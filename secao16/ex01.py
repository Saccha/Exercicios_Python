"""
1.Crie uma classe para representar uma pessoa, como os atirbutos privados de
nome, idade e altura. Crie os métodos públicos necessários para sets e gets e
também um método para imprimir os dados de uma pessoa.
"""

class Pessoa:
  def __init__(self,nome,idade,altura):
    self.nome = nome
    self.idade = idade
    self.altura = altura
  def setNome(self,nome):
    self.nome = nome
  def setIdade(self,idade):
    self.idade = idade
  def setAltura(self,altura):
    self.altura = altura
  def getNome(self,nome):
    return self.nome
  def getIdade(self):
    return self.idade
  def getAltura(self):
    return self.altura

dados = Pessoa('Sabrina', 20, 1.66)
print('Nome:', dados.nome)
print('Idade:', dados.idade)
print('Altura:', dados.altura)
