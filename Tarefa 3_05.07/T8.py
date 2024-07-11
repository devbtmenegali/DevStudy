#Maior número: Faça um programa que recebe vários números e encontra o maior número recebido 
#(pare quando o número 0 for recebido) e exibe o resultado.

def encontrar_maior_numero(*numeros):       # O asterisco antes de numeros indica que a função aceita um número variável de argumentos. Esses argumentos são empacotados em uma tupla chamada numeros.
    maior_numero = float('-inf')            # A variável inicia no menor valor possível ('-inf').                       #
    
    for n in numeros:
        
        if maior_numero == 0:
            break
        if n > maior_numero:                # Se o número atual (n) for maior que o valor armazenado em maior_numero, maior_numero é atualizado para o valor de n
            maior_numero = n
        
    return maior_numero                     # Após verificar todos os números (ou encontrar um 0), a função retorna o valor armazenado em maior_numero, que representa o maior número encontrado.

numeros = [4, 7, 9, 10, 5, 1]               # Lista de números
resultado = encontrar_maior_numero(*numeros) # Desempacota a lista como argumentos
print("O maior número recebido foi", resultado)