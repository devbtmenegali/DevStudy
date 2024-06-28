valor = float(input())
notes = int(valor)
coins = int(round((valor - notes)*100))

notas = [100, 50, 20, 10, 5, 2]
moedas = [100, 50, 25, 10, 5, 1]

print("NOTAS:")

for nota in notas:                                      
    quantidade = notes // nota                              
    notes %= nota
                                      
    print(f"{quantidade} nota(s) de R$ {nota:.2f}")

print("MOEDAS:")

for moeda in moedas[1:]:                                      
    quant = coins // moeda                              
    coins %= moeda
                                      
    print(f"{quant} moeda(s) de R$ {moeda/100:.2f}")
    