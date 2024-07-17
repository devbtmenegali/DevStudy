'''
Pedro está organizando sua coleção de filmes e anotou os nomes de 5 filmes que quer assistir. 
Crie um programa em Python que permita adicionar novos filmes, remover filmes já assistidos e 
imprimir a lista atualizada de filmes para assistir.
'''
colecao_filmes = []

def escolha():
    print(f"Bem-vindo a lista de filmes do Pedro")
    print(f"Digite 1 para acrescentar")
    print(f"Digite 2 para remover")
    print(f"Digite 3 para trocar")
    escolha = input("Escolha a opção:")
    
    if escolha == 0:
        print("Saindo do programa. Até logo!")
            
    elif escolha == 1:
        adicionar_filmes()

    elif escolha == 2: 

    #elif escolha == 3: 
        trocar_filmes()

    else:
        print("Opção inválida ou lista de filmes vazia.")

escolha()

def adicionar_filmes():
    
    for f in range(1,6):
        filme = input(f"Digite o título do filme {f}:").rstrip()
        colecao_filmes.append(filme)

    print(colecao_filmes)

adicionar_filmes()

def remover_filmes(colecao_filmes):
    
    for f in range():
        filme = input(f"Digite o nome do filme a ser removido:")
        colecao_filmes.remove(colecao_filmes)
    
    print(colecao_filmes)
    
remover_filmes()

escolha()

#def trocar_filmes():

