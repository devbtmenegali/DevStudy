'''
Verificação de palíndromo: Escreva um código que verifique se uma palavra é um palíndromo. 
Palíndromos são palavras, frases, números ou outras sequências de caracteres que, quando lidas de 
trás para frente, EX: OVO.
'''

def conta_pares_impares(inicio, fim):
    count_pares = 0
    count_impares = 0
    
    for i in range(inicio, fim + 1):
        if i % 2 == 0:
            count_pares += 1
        else:
            count_impares += 1
    
    return count_pares, count_impares

# Exemplo de uso:
inicio = 1
fim = 20
pares, impares = conta_pares_impares(inicio, fim)
print(f"Número de Pares: {pares}")
print(f"Número de Ímpares: {impares}")