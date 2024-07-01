product_prices = {1: 4.00, 2: 4.50, 3: 5.00, 4: 2.00, 5: 1.50}

code, quantity = map(int, input().split())

if code in product_prices:
    price = product_prices[code]
    total = quantity * price
    print(f"Total: R$ {total:.2f}")
else:
    print("Código Inválido")
    