#Fernanda está preparando uma lista de convidados para sua festa e já listou 6 pessoas. 
#Ela quer adicionar um novo convidado na quarta posição da lista. 
#Crie um programa em Python que receba os nomes dos convidados e insira o novo convidado na posição correta.

def convidados_festa():
    lista_da_festa = []

    for i in range (1,7):
        convidado = input("Digite o nome do convidado:").strip()
        lista_da_festa.append(convidado)

    print(lista_da_festa)
    novo_convidado = input("Você quer incluir mais algum convidado?")

    if novo_convidado.lower() == "sim":
        incluir_convidado()

    elif novo_convidado.lower() == "nao":
        print("A FESTA ESTÁ COMPLETA!")
    
    else:
        print("Digite um valor válido!")

    return lista_da_festa



convidados_festa()

#def incluir_convidado():
