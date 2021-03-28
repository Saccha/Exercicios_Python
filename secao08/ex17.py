"""
17.Faça uma função que receba dois números inteiros positivos
por parâmetro e retorne a soma dos N números inteiros existentes
entre eles.
"""
def entre_numeros(num1,num2):
    soma = 0
    if num1 // 1 == num1 and num2 // 1 == num2:
        if num1 >= num2:
            for i in range(num2+1, num1, 1):
                soma += i
        elif num2 >= num1:
            for i in range(num1+1, num2, 1):
                soma += i
        return soma
num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

print(f"\nA soma dos N entre os números recebidos: {entre_numeros(num1, num2)}")
