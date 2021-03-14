'''
21. Escreva o menu de opções abaixo. Leia A opção do usuário e execute A operação escolhida.
Escreva uma mensagem de erro se A opção for inválida.
    Escolha A opção:
    1- Soma de 2 números.
    2- Diferença entre números (maior pela menor).
    3- Produto entre 2 números.
    4- Divisão entre 2 números (o denominador não pode ser zero).
'''
print('''	
Escolha A opção:
1- Soma de 2 números.
2- Diferença entre números (maior pelo menor).
3- Produto entre 2 números.
4- Divisão entre 2 números (o denominador não pode ser zero).
''')
escolha = int(input('Escolha: '))
x = float(input('Um número: '))
y = float(input('Outro número: '))

if escolha == 1:
    resultado = x + y
    print(f'{x} + {y} = {resultado}')

elif escolha == 2:
    if x > y:
        resultado = x - y
        print(f'{x} - {y} = {resultado}')

    else:
        resultado = y - x
        print(f'{y} - {x} = {resultado}')

elif escolha == 3:
    resultado = x * y
    print(f'{x} * {y} = {resultado}')

elif escolha == 4:
    if x > y:
        if y != 0:
            resultado = x / y
            print(f'{x} / {y} = {resultado}')

    else:
        if x != 0:
            resultado = y / x
            print(f'{y} / {x} = {resultado}')
