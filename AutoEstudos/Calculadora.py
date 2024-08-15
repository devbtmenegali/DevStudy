
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
            if N2 == 0:
                print("Erro: divisão por zero!")
            
            else:
                divisao = N1/N2
                print (divisao)

        else: 
            print("Erro no operador!")
                 
    except ValueError:
        print("Digite um valor válido!")

calculadora_basica()