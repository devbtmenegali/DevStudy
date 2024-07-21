#Escreva uma função que exibe um menu de opções e continua executando até que o usuário escolha sair.

def menu():
    lanches = ["Pizza", "X-Salada", "Hamburguer", "Macarronada"]

    while True:  
        for item in lanches:
            print(item)

        sair = input("Digite 's' para sair ou qualquer outra tecla para continuar: ")
        
        if sair.lower() == 's':  
            print("Você saiu!")
            break  

menu()

