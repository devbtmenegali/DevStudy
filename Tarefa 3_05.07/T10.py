#Soma: Faça um programa que recebe um número como argumento e calcula a soma de todos os números de 1 até o 
#número recebido e exibe o resultado.

def calcular_soma(n):
    soma = 0

    for i in range(1, n +1):
        soma += i
    
    return soma

n = 15
resultado = calcular_soma(n)
print("A soma é", resultado)