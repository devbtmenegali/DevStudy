# Média: Faça um programa que recebe vários números e calcula a média dos números recebidos 
# (pare quando o número 0 for recebido) e exibe o resultado.

def calcular_media(*numeros):
    soma, count = 0, 0
    for i in range(len(numeros)):
        n = numeros[i]
        if n == 0:
            break
        soma += n
        count += 1
    if count == 0:
        return "Nenhum número foi recebido."
    else:
        return soma / count

# Exemplo de uso da função
resultado = calcular_media(3, 5, 7, 0, 2, 8)
if isinstance(resultado, str):
    print(resultado)
else:
    print("A média dos números recebidos é", resultado)