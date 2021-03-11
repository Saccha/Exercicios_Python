#39. A importância de R$ 780.000.00 será dividida entre três ganhadores de um concurso.
# Sendo que da quantia total:
#   * O primeiro ganhador receberá 46%;
#   * O segundo receberá 32%;
#   * O terceiro receberá o restante;
# 
#   Calcule e imprima a quantia ganhada por cada um dos ganhadores.



valor_total = 78000000 
ganhador_1 =  (0.46*valor_total) 
ganhador_2 =  (0.32*valor_total)
ganhador_3 = valor_total - (ganhador_1+ganhador_2)

print(''''
    R$780.000.00 será dividida entre três ganhadores de um concurso.
    * O primeiro ganhador receberá {0}.
    * O segundo  receberá {1}.
    * O terceiro receberá {2:.2f}
'''.format(ganhador_1,ganhador_2,ganhador_3))
