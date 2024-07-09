#Contagem de caracteres: Escreva um código que conte quantas letras maiúsculas há em uma frase.

def contagem_caracteres(frase): 
    total_maiusculas = 0

    for letra in frase:
        if letra.isupper():
            total_maiusculas += 1

    return total_maiusculas

frase = "Esta é Uma Frase Aleatória para Testar."
resultado = contagem_caracteres(frase)  
print(f"Total de letras maiúsculas: {resultado}")