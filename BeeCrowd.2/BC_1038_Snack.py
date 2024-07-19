product_prices = {1: 4.00, 2: 4.50, 3: 5.00, 4: 2.00, 5: 1.50}

code, quantity = map(int, input().split())

if code in product_prices:
    price = product_prices[code]            # Pega o preço do produto
    total = price * quantity                # Calcula o custo
    
    print(f"Total: R$ {total:.2f}")         # Imprimir preço total

else:
    print("Código inválido")                # Mensagem de Erro