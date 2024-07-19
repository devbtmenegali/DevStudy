#Você está desenvolvendo um programa para gerenciar uma loja online. 
#A loja possui várias categorias de produtos e cada categoria tem sua própria lista de produtos. 
#Crie um programa em Python que combine todas as listas de produtos em uma única lista e exiba a lista 
#final de produtos disponíveis na loja.

lista_produtos = []
lista_tenis = []
lista_roupas = []
lista_cama = []

def categoria_tenis ():
    lista_tenis = []
    while True:
        marcas_tenis = input("Adicione uma marca de tenis:")

        if marcas_tenis == "finalizar":
            print(f"A lista de tenis contém: {lista_tenis}")
            break
        elif marcas_tenis == "roupa":
            categoria_roupa()

        lista_tenis.append(marcas_tenis)
    
    print(f"A lista de tenis contém: {lista_tenis}")
    return lista_tenis

def categoria_roupa ():
    lista_roupas = []
    while True:
        marcas_roupas = input("Adicione uma marca de roupas:")

        if marcas_roupas == "finalizar":
            break
        elif marcas_roupas == "cama":
            categoria_cama()

        lista_roupas.append(marcas_roupas)
    
    print(f"A lista de roupa contém: {lista_roupas}")
    return lista_roupas

def categoria_cama ():
    lista_cama = []
    while True:
        marcas_cama = input("Adicione uma marca de roupa de cama:")

        if marcas_cama == "finalizar":
            break
        elif marcas_cama == "listar":
            print(lista_produtos)

        lista_cama.append(marcas_cama)
    
    print(f"A lista de roupa de cama contém: {lista_cama}")
    return lista_cama


lista_tenis = categoria_tenis()
lista_roupas = categoria_roupa()
lista_cama = categoria_cama()

lista_produtos.extend(lista_tenis)
lista_produtos.extend(lista_roupas)
lista_produtos.extend(lista_cama)    
print(lista_produtos)

categoria_tenis()
categoria_roupa()
categoria_cama()


