ddd = {61: 'Brasilia', 71: 'Salvador', 11: 'Sao Paulo', 21: 'Rio de Janeiro', 32: 'Juiz de Fora', 19: 'Campinas', 27: 'Vitoria', 31: 'Belo Horizonte'}

code = int(input())

if code in ddd:
    print(f"{ddd[code]}")

else:
    print(f"DDD nao cadastrado")
