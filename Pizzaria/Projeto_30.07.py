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

    for codigo in ingredientes.keys():  # Itera sobre as chaves (códigos)
        print(f"{codigo} - {ingredientes[codigo]}")  # Acessa o nome pelo código

    return ingredientes

def escolher_ingredientes(ingredientes):
    ingredientes_escolhidos = []

    while len(ingredientes_escolhidos) < 4:
        ingrediente_escolher = input("Digite o código do ingrediente ou S(sair): ").upper()

        if ingrediente_escolher == "S":
            break  # Remove a chamada para fechar_pedido() aqui

        if ingrediente_escolher in ingredientes:
            ingredientes_escolhidos.append(ingrediente_escolher)
        else:
            print("Escolha uma opção válida!")

    total_preco_ingredientes = len(ingredientes_escolhidos) * 3.00
    return ingredientes_escolhidos, total_preco_ingredientes

def fechar_pedido(pizza_escolher, preco_da_pizza, ingredientes, total_preco_ingredientes):
    
    print(f"Item: {pizza_escolher} - {preco_da_pizza}")
    print(f"Adicional: {ingredientes} - {total_preco_ingredientes}")  # Corrigido o nome da variável
    valor_total = preco_da_pizza + total_preco_ingredientes
    print(f"Valor Total a pagar: {valor_total:.2f}")

    apresentar_formas_pagamento()  # Chama a função para apresentar as formas de pagamento

def apresentar_formas_pagamento():
    formas_de_pagamento = {"P": "Pix",
                           "D": "Cartão",
                           "M": "Dinheiro"}

    for codigo, forma_pagamento in formas_de_pagamento.items():  # Corrigido o nome da variável no loop
        print(f"{codigo} - {forma_pagamento}")

    return formas_de_pagamento

def escolher_pagamento(formas_de_pagamento):

    while True:

        try:
            pagamento = input("Digite o código conforme a forma de pagamento: ").upper()

            if pagamento in formas_de_pagamento:
                return formas_de_pagamento[pagamento]

            else:
                print("Código Inválido")

        except ValueError:
            print ("Digite um valor válido!")

def pagamento_escolhido(pagamento):

    if pagamento == "P":
        print("Use o QR-Code para pagar")

    elif pagamento == "D":
        print("Aproxime o cartão da máquina!")

    elif pagamento == "D":
        print(f"Deposite o dinheiro na carteira")

    else:
        print ("A opção escolhida é inválida!")

    print("Muito obrigado pela preferência!")

def main():
    cardapio = exibir_cardapio()
    pizza_escolhida = escolher_pizza(cardapio)  # Obtém o nome da pizza
    codigo_pizza = list(cardapio.keys())[list(cardapio.values()).index(pizza_escolhida)] # Obtém o código da pizza a partir do nome
    preco_pizza = preco_da_pizza(codigo_pizza)  # Passa o código da pizza para preco_da_pizza

    ingredientes = exibir_ingredientes()
    ingredientes_escolhidos, total_preco_ingredientes = escolher_ingredientes(ingredientes)

    fechar_pedido(pizza_escolhida, preco_pizza, ingredientes_escolhidos, total_preco_ingredientes) 

    formas_de_pagamento = apresentar_formas_pagamento() 
    forma_pagamento_escolhida = escolher_pagamento(formas_de_pagamento) 

    pagamento_escolhido(forma_pagamento_escolhida)


if __name__ == "__main__":
    main()


'''

'''