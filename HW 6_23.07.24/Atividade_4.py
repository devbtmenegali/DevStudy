'''Crie um programa em Python que solicite entradas ao usuário até que ele insira um EOF (Ctrl+D ou Ctrl+Z). 
Utilize try/except para lidar com a exceção EOFError.'''

def entradas_aleatorias():

    while True:

        try:

            entrada = input("Digite algo: ")
            print (f"Foi digitado {entrada}")
        
        except EOFError:
            print("Você digitou algo que levou ao fim!")
            break

entradas_aleatorias()