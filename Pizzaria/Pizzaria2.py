def apresentar_cardapio():

    cardapio = {1:"Calabresa",
                2:"Frango",
                3:"Portuguesa",
                4:"4 Queijos",
                5:"Mussarela"}

    for codigo, sabor in cardapio.items():
        print(f"{codigo} - {sabor}")

    return cardapio

def escolher_pizza (cardapio):

    while True:

        try:
            selecionar_pizza = int(input("Digite o Código da pizza para escolher:"))

            if selecionar_pizza in cardapio:
                return cardapio[selecionar_pizza]
            
            else:
                print("Código inexistente, tente novamente")

        except ValueError:
            print("Digite um valor válido!")


def preco_da_pizza(selecionar_pizza):

    if selecionar_pizza == 1 or selecionar_pizza == 2:
        return 30.00

    elif selecionar_pizza == 3 or selecionar_pizza == 4:
        return 35.00

    elif selecionar_pizza == 5:
        return 40.00

def apresentar_adicional():

    adicional = {1:"Queijo", 2:"Ovo", 3:"Tomate"}

    for codigo_adicional, produtos_extras in adicional.items():
        print(f"{codigo_adicional} - {produtos_extras}")

    return adicional


#def escolher_adicional():

#def apresentar_pedido_finalizado():

#def apresentar_forma_de_pagamento():

#def escolher_forma_de_pagamento():

#def apresentar_nota_fiscal():


def main():

    cardapio = apresentar_cardapio()
    pizza_escolhida = escolher_pizza(cardapio)
    preco_pizza = preco_da_pizza(pizza_escolhida)

    apresentar_adicional()

if __name__ == "__main__":

    main()
