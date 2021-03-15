"""
37. As tarifas de certo parque de estacionamento são as seguintes:
- 1ª e 2ª hora > R$ 1,00 cada
- 3ª e 4ª hora > R$ 1,40 cada
- 5ª hora e seguintes > R$ 2,00 cada
O número de horas a pagar é sempre inteiro e arredondado por excesso. Deste modo,
quem estacionar durante 61 minutos pagará por duas horas, que é o mesmo que pagaria
se tivesse permanecido 120 minutos. Os momentos de chegada ao parque e partida
deste são apresentados na forma de pares inteiros, representando horas e minutos.
Por exemplo, o par 12 50 representará "dez para uma da tarde". Pretende-se criar um
programa que, lidos pelo teclado os momentos de chegada e de partida, escreva na tela
o preço cobrado pelo estacionamento. Admite-se que a chegada e a partida se dão com
intervalo não superior a 24 horas. Portanto, se uma dada hora de chegada for superior
à da partida, isso não é superior a 24 horas. portanto, se uma dada hora de chegada for superior
à da partida, isso não é uma situação de erro, antes significará que a partida ocorreu no
dia seguinte ao da chegada.
"""

chegada = int(input("Digite a hora de chegada: "))
partida = int(input("Digite a hora de saída: "))

permanencia = partida - chegada

print(f"Tempo de permanência: {permanencia} minutos.")

if permanencia <= 120:
    custo = 1.00
    print(f"O preço é de R${custo}")

elif 120 < permanencia <= 240:
    custo = 1.40
    print(f"O preço é de R${custo}")

elif permanencia > 300:
    custo = 2.00
    print(f"O preço é de R${custo}")
