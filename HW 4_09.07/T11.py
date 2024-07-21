#Escreva uma função que calcula o fatorial de um número.

def fatorial(n):
    resultado = 1
    while n > 0:
        resultado *= n
        n -= 1
    return resultado

print(fatorial(3))
