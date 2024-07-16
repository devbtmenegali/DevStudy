'''
Pedro está organizando sua coleção de filmes e anotou os nomes de 5 filmes que quer assistir. 
Crie um programa em Python que permita adicionar novos filmes, remover filmes já assistidos e 
imprimir a lista atualizada de filmes para assistir.
'''
def escolha():
    print(f"Bem-vindo a lista de filmes do Pedro")
    print(f"Digite 1 para acrescentar")
    print(f"Digite 2 para remover")
    print(f"Digite 3 para trocar")
    escolha = int(input("Escolha a opção:"))
    colecao_filmes = []
    
    if escolha == 1:
        adicionar_filmes()
    
    elif escolha == 2:
        remover_filmes()
    
    elif escolha == 3:
        trocar_filmes()
    
    else: 
        print(f"Valor incorreto, escolha a opção válida!")
        escolha = int(input("Escolha a opção:"))
        
def adicionar_filmes(colecao_filmes):
    
    for f in range(1,6):
        filme = input(f"Digite o título do filme {f}:").rstrip()
        colecao_filmes.append(colecao_filmes)

    print(colecao_filmes)

def remover_filmes(colecao_filmes):
    
    
    
    
    
def trocar_filmes():

