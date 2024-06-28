idade = int (input ("Qual sua idade, 12, 16 ou 21?"))
valor = 20
resultado = 0

match idade:                            #estrutura -> match + variável + :
    case 12:
        print ("Você só pode assistir filmes Disney")
    case 16:
        print ("Você só pode assistir filmes Marvel")
    case 21:
        print ("Você só pode assistir filmes W. Bross")
    case _:
        print ("Vai estudar!")
    
