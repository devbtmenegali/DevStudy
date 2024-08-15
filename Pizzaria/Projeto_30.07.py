
def exibir_cardapio():

    cardapio = {1: "Calabresa",
                2: "Portuguesa",
                3: "Frango",
                4: "4 Queijos",
                5: "Carne de Sol"}

    for codigo, produto in cardapio.items():            #items remete as variaveis codigo e produto ao dicionário.
        print (f" {codigo} - {produto}")
    
    return cardapio

def escolher_pizza(cardapio):

    while True:

        try:

            pizza_escolher = int(input("Digite o código para escolher a pizza: "))

            if pizza_escolher in cardapio:
                return cardapio[pizza_escolher]

            else:
                print("Escolha uma opção válida!")

        except ValueError:
            print("Digite um valor inteiro!")

def preco_da_pizza(pizza_escolher):

    if pizza_escolher == 1 or pizza_escolher == 2:
        return 25.00
    
    elif pizza_escolher == 3 or pizza_escolher == 4:
        return 30.00
    
    elif pizza_escolher == 5:
        return 35.00

    else:
        return None

def exibir_ingredientes():

    ingredientes = {"A":"Catupiri",
                    "B":"Cheedar", 
                    "C":"+Queijo"}

    for codigo,ingredientes in ingredientes.items():
        print(f"{codigo} - {ingredientes}")
    
    return ingredientes

def escolher_ingredientes(ingredientes):

    #ingredientes_totais = exibir_ingredientes()
    ingredientes_escolhidos = []
    
    while len(ingredientes_escolhidos) < 3:
    
        ingredientes_escolher = input ("Digite o código do ingrediente ou S(sair):").upper()
                
        if ingredientes_escolher in ingredientes:
            ingredientes_escolhidos.append(ingredientes_escolher)

        if ingredientes_escolher == "S":
            break
    
    total_preco_ingredientes = len(ingredientes_escolhidos) * 3.00
    return total_preco_ingredientes

def fechar_pedido():

    print(f"Item: {escolher_pizza} - {preco_da_pizza}")
    print(f"Adicional: {ingredientes_escolhidos} - {total_preco_ingredientes}")
    valor_total = preco_da_pizza + total_preco_ingredientes
    print(f"Valor Total a pagar: {valor_total:.2f}")
    
def apresentar_formas_pagamento():

    formas_de_pagamento = {"P": "Pix",
                           "D": "Cartão",
                           "M": "Dinheiro"}

    for codigo, formas_de_pagamento in formas_de_pagamento.items():
        print(f"{codigo} - {formas_de_pagamento}")

def escolher_pagamento():

    while True:

        try:
            pagamento = input("Digite o código conforme a forma de pagamento: ")

            if pagamento in formas_de_pagamento:
                return formas_de_pagamento[pagamento]

            else:
                print("Código Inválido")

        except ValueError:
            print ("Digite um valor válido!")



def main ():

    cardapio = exibir_cardapio()
    escolher = escolher_pizza(cardapio)
    preco_pizza = preco_da_pizza(escolher)
    
    ingredientes = exibir_ingredientes()
    escolher_ingredientes(ingredientes)
    preco_ingrediente = preco_ingredientes()
    
    fechar_pedido(preco_pizza, preco_ingrediente)
    
    #apresentar_formas_pagamento()
    #escolher_pagamento()
    #finalizacao_pedido()

if __name__== "__main__":

    main()