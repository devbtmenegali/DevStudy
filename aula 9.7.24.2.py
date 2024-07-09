def tabuada ():
    i = int(input('Digite um número'))
    multiplicador = 1
    
    while multiplicador <= 10:
        resultado = i * multiplicador
        print(f"{i} x {multiplicador} = {resultado}")

        multiplicador += 1

tabuada()