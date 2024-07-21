#Crie um programa que solicite ao usuário um número inicial e a razão de uma sequência geométrica. 
#O programa deve exibir os primeiros 10 termos dessa sequência.

def termo_pg(a1, q, n):
    
    return a1 * q**(n - 1)

a1 = int(input("Digite um número:"))
q = int(input("Digite a progressão:"))
n = 10

for i in range(1, n + 1):
    resultado = termo_pg(a1, q, i)
    print(f"Termo {i}: {resultado}")
