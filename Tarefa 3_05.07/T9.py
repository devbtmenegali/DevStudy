# Média: Faça um programa que recebe vários números e calcula a média dos números recebidos 
# (pare quando o número 0 for recebido) e exibe o resultado.

def calcular_media(*numeros):                   # O nome calcular_media --> caixa. O *numeros --> podemos colocar quantas maçãs quisermos dentro da caixa.
    soma, count = 0, 0                          # Temos 2 cestas: uma com tamanho das maças e outra com a quantidade.
    for i in range(len(numeros)):               # A caixa tem um ajudante que pega cada maçã da caixa, uma por uma. Código: Essa linha diz ao ajudante: "Comece a pegar as maçãs! Vá da primeira até a última."
        n = numeros[i]                          
        if n == 0:
            break
        soma += n                               # "Some o peso da maçã ao total da cesta da soma."
        count += 1                              # "Adicione 1 à cesta do contador."
    if count == 0:
        return "Nenhum número foi recebido."
    else:
        return soma / count                     # "Calcule a média dividindo a soma pelo número de maçãs e diga o resultado."

resultado = calcular_media(3, 5, 7, 0, 2, 8)
if isinstance(resultado, str):
    print(resultado)
else:
    print("A média dos números recebidos é", resultado)