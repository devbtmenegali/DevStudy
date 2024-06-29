
valor = float(input())                                     

valor_centavos = int(valor * 100)                           # Converte para centavos (integer)

notas = [10000, 5000, 2000, 1000, 500, 200]                 # em centavos
moedas = [100, 50, 25, 10, 5, 1]

print("NOTAS:")

for nota in notas:
    quantidade = valor_centavos // nota
    print(f"{quantidade} nota(s) de R$ {nota/100:.2f}")     # Converter para reais
    valor_centavos %= nota

print("MOEDAS:")
for moeda in moedas:
    quantidade = valor_centavos // moeda
    print(f"{quantidade} moeda(s) de R$ {moeda/100:.2f}")   # Converter para reais
    valor_centavos %= moeda
