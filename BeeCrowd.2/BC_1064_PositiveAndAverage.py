
def positives_and_average():
   
    positive_numbers = 0  
    numeros = []

    for n in range (6):
        n = float(input( ))
        numeros.append(n)
        average = sum(numeros)/len(numeros)

        if n > 0:
            positive_numbers += 1  

    print(f"{positive_numbers} valores positivos")
    print(f"{average:.1f}")  

positives_and_average()