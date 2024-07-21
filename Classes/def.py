#Crie uma função chamada calcular que receba dois números e um operador (+, -, *, /) como argumentos. 
# A função deve realizar a operação correspondente e retornar o resultado.

def calcular(num1, num2, operador):
    if operador == '+':
        return num1 + num2
    elif operador == '-':
        return num1 - num2
    elif operador == '*':
        return num1 * num2
    elif operador == '/':
        if num2 == 0:
            print("Erro: Divisão por zero não é permitida.")
            return None
        else:
            return num1 / num2
    else:
        print("Erro: Operador inválido. Use +, -, * ou /.")
        return None

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
operador = input("Digite o operador (+, -, *, /): ")

resultado = calcular(num1, num2, operador)  # Chama a função e armazena o resultado

if resultado is not None:  # Verifica se a operação foi válida
    print(f"Resultado: {resultado}")