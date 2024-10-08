'''
Pedro está organizando sua coleção de filmes e anotou os nomes de 5 filmes que quer assistir. 
Crie um programa em Python que permita adicionar novos filmes, remover filmes já assistidos e 
imprimir a lista atualizada de filmes para assistir.
'''
colecao_filmes = []

def escolha():
    while True:
        print(f"Bem-vindo a lista de filmes do Pedro")
        print(f"Digite 1 para acrescentar")
        print(f"Digite 2 para remover")
        print(f"Digite 3 para trocar")
        print(f"Digite 0 para sair")
        escolha = input("Escolha a opção: ")

        # Converter a entrada para inteiro
        if escolha.isdigit():
            escolha = int(escolha)
        else:
            print("Opção inválida. Digite um número.")
            continue

        if escolha == 0:
            print("Saindo do programa. Até logo!")
            break

        elif escolha == 1:
            adicionar_filmes()

        elif escolha == 2:
            remover_filmes()

        elif escolha == 3: 
            trocar_filmes()

        else:
            print("Opção inválida ou lista de filmes vazia.")

def adicionar_filmes():
   
    while True:
        filmes_str = input("Digite o nome do filme ou (s)air:").strip()
        if filmes_str.lower() == 's':
            break
        colecao_filmes.append(filmes_str)    
    
    print("Filmes adaicionados com sucesso!")
    print(colecao_filmes)

def remover_filmes():

    while True:
        filmes_str = input("Escreva o nome do filme a ser retirado:")
        if filmes_str.lower() == "s":
            break
        colecao_filmes.remove(filmes_str)

    print("Filme(s) removidos com sucesso")
    print(colecao_filmes)

def trocar_filmes():

    while True:
        filmes_str = input("Você quer retirar qual filme:")
        if filmes_str.lower() == "s":
            break
        colecao_filmes.remove(filmes_str)

        trocar = input("Agora, qual filme você quer acrescentar:")
        colecao_filmes.append(trocar)

    print("Filme(s) trocados com sucesso")
    print(colecao_filmes)

escolha()
