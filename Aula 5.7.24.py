#Descrição: Escreva uma função fatorial que receba um número inteiro e retorne o seu fatorial.

def fatorial(n):
    resultado = 1    
    
    for f in range (1, n+1):
        print(f)
        resultado = resultado * f
        #print (resultado)
    
    return resultado

def tabuada (x):

    for t in range (1, 11):
        multiplicacao = t * x

        print(f"{x} x {t} = {multiplicacao}")
        
print(tabuada(4))


print(fatorial(5))


 

