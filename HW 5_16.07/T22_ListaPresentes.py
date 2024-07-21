#Paula está fazendo uma lista de presentes para o Natal. 
#Crie um programa em Python que permita adicionar itens à 
#lista de presentes e exibir a lista final.

lista_de_presentes = []

def adicionar_presentes():
    
    while True:
        presentes = input("Adicione um presente ou (S) para fechar lista: ").strip()

        if presentes.lower() == "s":
            break
        
        lista_de_presentes.append(presentes)

    print("LISTA DE PRESENTES.")
    print(lista_de_presentes)
    
adicionar_presentes()
