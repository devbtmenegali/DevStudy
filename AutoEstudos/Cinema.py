colecao_filmes = []

def escolha():
    while True:
        print("\nBem-vindo à lista de filmes do Pedro")
        print("1. Adicionar filmes")
        print("2. Remover filmes")
        print("3. Trocar filmes")
        print("0. Sair")

        escolha_str = input("Escolha a opção: ")
        if escolha_str.isdigit() and 0 <= int(escolha_str) <= 3:
            escolha = int(escolha_str)

            if escolha == 0:
                print("Saindo do programa. Até logo!")
                break

            elif escolha == 1:
                adicionar_filmes()

            elif escolha == 2 and colecao_filmes:
                remover_filmes()

            elif escolha == 3 and colecao_filmes:
                trocar_filmes()

        else:
            print("Opção inválida. Digite um número entre 0 e 3.")

def adicionar_filmes():
    while True:
        num_filmes_str = input("Quantos filmes deseja adicionar? ")
        if num_filmes_str.isdigit() and int(num_filmes_str) > 0:
            num_filmes = int(num_filmes_str)
            break
        else:
            print("Número inválido. Digite um número inteiro positivo.")

    for i in range(num_filmes):
        filme = input(f"Digite o título do filme {i+1}: ").strip()
        colecao_filmes.append(filme)

    print("Filmes adicionados com sucesso!")
    print(colecao_filmes)

def remover_filmes():
    print("Filmes na coleção:")
    for i, filme in enumerate(colecao_filmes):
        print(f"{i+1}. {filme}")

    indice_str = input("Digite o número do filme a ser removido: ")
    if indice_str.isdigit() and 1 <= int(indice_str) <= len(colecao_filmes):
        indice = int(indice_str) - 1
        filme_removido = colecao_filmes.pop(indice)
        print(f"O filme '{filme_removido}' foi removido com sucesso!")
        print(colecao_filmes)
    else:
        print("Índice inválido.")
        remover_filmes()  # Chama a si mesma para tentar novamente

def trocar_filmes():
    print("Filmes na coleção:")
    for i, filme in enumerate(colecao_filmes):
        print(f"{i+1}. {filme}")

    indice_str = input("Digite o número do filme a ser substituído: ")
    if indice_str.isdigit() and 1 <= int(indice_str) <= len(colecao_filmes):
        indice = int(indice_str) - 1
        novo_filme = input("Digite o novo título do filme: ").strip()
        colecao_filmes[indice] = novo_filme
        print(f"O filme foi substituído por '{novo_filme}' com sucesso!")
        print(colecao_filmes)
    else:
        print("Índice inválido.")
        trocar_filmes()  # Chama a si mesma para tentar novamente

# Inicia o programa
escolha()