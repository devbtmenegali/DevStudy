# Crie um programa que solicite um número inteiro positivo ao usuário e verifique se ele é um número perfeito. 
# Um número perfeito é aquele que é igual à soma de seus divisores positivos próprios (excluindo ele mesmo).


num = int(input("Digite um número inteiro positivo: "))
# forma de calcular a soma dos divisores próprios de um número --> "compreensão de lista"
soma_divisores = sum(i for i in range(1, num) if num % i == 0)

if soma_divisores == num:
    print(f"{num} é um número perfeito.")
else:
    print(f"{num} não é um número perfeito.")