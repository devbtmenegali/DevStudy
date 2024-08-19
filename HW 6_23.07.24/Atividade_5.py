'''João está criando uma calculadora que realiza operações básicas (adição, subtração, multiplicação e divisão). 
Crie um programa em Python que permita ao usuário escolher a operação e fornecer os números necessários. 
Utilize try/except para lidar com exceções aritméticas (ArithmeticError), como divisão por zero.'''

def calculadora_basica():
    
    try:

        N1 = float(input("Digite o número:"))
        Operador = input("Digite a operação:")
        N2 = float(input("Digite o número:"))

        if Operador == "+":
            soma = N1 + N2
            print(soma)

        elif Operador == "-":
            subtracao = N1 - N2
            print(subtracao)

        elif Operador == "*":
            multiplicacao = N1 * N2
            print(multiplicacao)

        elif Operador == "/":
            divisao = N1/N2
            print (divisao)
                     
    except ArithmeticError:
        print("Digite um valor válido!")

calculadora_basica()