'''
Divisíveis por 6: Escreva um código que imprima os números de 0 a 60 que são divisíveis por 6. 
Números divisíveis por 6 são aqueles que, quando divididos por 6, resultam em um número inteiro, 
ou seja, não deixam resto.Para que um número seja divisível por 6, ele precisa ser divisível tanto por 2 quanto por 3.
'''

def multiplos6():
    
    for m6 in range(6, 60*1,6):
        print(m6)

multiplos6()

