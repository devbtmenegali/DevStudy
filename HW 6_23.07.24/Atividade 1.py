'''Ana está tentando acessar um índice específico de uma lista. Crie um programa em Python que solicite a lista e o índice,
tente acessá-lo e utilize try/except/else/finally para lidar com exceções como IndexError.'''

def conhecer_a_lista():
    carros = ['gol', 'prisma', 'tucson', 'cobalt']

    try:
        solicitacao_da_lista = input("Digite 1 para conhecer o menu ou 0 para sair: ")

        if solicitacao_da_lista == '1':  
            print(carros)
            indice = int(input("Digite o número do carro (0 a 3): "))  

            if 0 <= indice < len(carros):           # Verificar se o índice é válido
                escolha_indice = carros[indice]     # Acessar o elemento pelo índice
                print(f"Você escolheu o carro: {escolha_indice}")
            else:
                print("Índice inválido. Digite um número entre 0 e 3.")

        elif solicitacao_da_lista == '0': 
            print("Saindo...")

        else:
            print("Opção inválida. Digite 1 ou 0.")

    except ValueError:
        print("Entrada inválida. Digite um número.")

    finally:
        print("Obrigado por usar o sistema!") 

conhecer_a_lista()

