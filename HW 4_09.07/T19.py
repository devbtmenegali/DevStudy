#Crie um programa que exiba todos os números de Armstrong entre 1 e 1000. Um número de Armstrong 
# (também conhecido como número narcisista) é um número que é igual à soma de seus próprios dígitos elevados 
# à potência do número de dígitos.

def numero_armstrong(numero):
    num_str = str(numero)                                           # Converte o número em uma string
    num_digitos = len(num_str)                                      # Obtém o número de dígitos em num_str 
    soma = sum(int(digito) ** num_digitos for digito in num_str)    
    return soma == numero

print("Números de Armstrong entre 1 e 1000:")
for num in range(1, 1001):
    if numero_armstrong(num):
        print(num)