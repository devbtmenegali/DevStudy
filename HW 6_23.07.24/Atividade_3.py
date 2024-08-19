'''João está tentando dividir dois números fornecidos pelo usuário. Crie um programa em Python que solicite os números, 
realize a divisão e utilize try/except/else/finally para lidar com exceções como ZeroDivisionError.'''

def divisao ():

    try:
    
        N1 = float(input("Digite o primeiro número:"))
        N2 = float(input("Digite o segundo número"))
        Resultado = N1/N2

        if N2 != 0:
            print(Resultado)
        
        else:
            print("Digite um número válido")

    except ZeroDivisionError:
        print("O divisor deve ser diferente de zero!")

    finally:
        print("Você usou sistema de divisão!")

divisao()