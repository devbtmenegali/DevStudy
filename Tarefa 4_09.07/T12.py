#Crie uma função que implementa um jogo de adivinhação de números.

def adivinhar_numero(n):
    numero = int(input("Digite um número: "))

    while numero == n:
        print("Parabéns!Você Acertou!")
        break
    
    else:
        print("Número Errado, tente novamente!")
        numero = int(input("Digite um número: "))

adivinhar_numero(4)
