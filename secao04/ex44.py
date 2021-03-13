#44. Receba a altura do degrau de uma escada e a altura que o usuário deseja alcançar
# subindo a escada. Calcule e mostre quantos degraus o usuário deverá subir para 
# atingir seu objetivo.

degrau = float(input("Digite a altura de um degrau: "))
objetivo = float(input("Digite a altura que deseja alcançar: "))
meta = (objetivo / degrau)
print("Para atingir o objetivo terá que subir {0} degraus".format(meta))
