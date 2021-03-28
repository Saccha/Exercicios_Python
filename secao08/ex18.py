"""
18.Faça uma função que receba por parâmero dois valores X e Z.
Calcule e retorne o resultado de X elevado a Z para o programa principal.
Atenção não utilize nenhuma função pronta de exponenciação.
"""
def exponenciacao(num,exp):
  return num ** exp
num = int(input("Digite o número: "))
exp = int(input("Digite o expoente: "))
print(f"\n{num} ** {exp} = {exponenciacao(num,exp)}")
