#Crie um programa que solicite números inteiros ao usuário até que ele digite zero. 
# O programa deve calcular e exibir a soma de todos os números pares fornecidos.

def coletor_de_numeros():
    numeros = []                                # Cria uma lista vazia para armazenar os números
    while True:
        numero = int(input("Digite um número (0->sair): "))
        if numero == 0:
            break  
        numeros.append(numero)                  # Adiciona o número à lista
    print("Números digitados:", numeros)

    resultado_pares = 0

    for n in numeros:
        if n % 2 == 0:
            resultado_pares += n 

    print("A soma dos números pares é:", resultado_pares)
coletor_de_numeros()