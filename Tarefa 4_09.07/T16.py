
def fatorial(n):
    if n == 0:
        return 1
    else:
        return n * fatorial(n - 1)

def soma_digitos(numero):
    return sum(int(digito) for digito in str(numero))

numero = 5  
fat = fatorial(numero)
soma = soma_digitos(fat)

print(f"A soma dos dígitos do fatorial de {numero} ({fat}) é: {soma}")