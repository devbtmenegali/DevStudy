def media ():
    media_numeros = []

    while True:
        numero = float(input("Digite um número:"))
        media_numeros.append(numero)
        if numero == 0:
            break
    media_numeros.remove(0)
    total = sum(media_numeros)/len(media_numeros)
    print(f"{total}")

media()
