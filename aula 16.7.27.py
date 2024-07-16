#João foi ao supermercado e registrou os preços de 7 itens diferentes que comprou. 
#Crie um programa em Python que calcule o total gasto e a média dos preços dos itens.

def itens_supermercado():
    lista_produtos=[]   

    for x in range (1,8):
        preco_produtos = float(input(f"Acrescente o preço do produto {x:.2f}:"))
        lista_produtos.append(preco_produtos)

    soma_produtos = sum(lista_produtos)
    media_preco = soma_produtos/len(lista_produtos)
    print(f"O total da lista é: R$ {soma_produtos:.2f}")
    print(f"A média do preço dos produtos é: R$ {media_preco:.2f}")

itens_supermercado()


