
def positives_and_average():
   
    positive_numbers = []  
    n_positive_numbers = 0

    for n in range (6):
        n = float(input( ))
        #numeros.append(n)
        

        if n > 0:
            positive_numbers.append(n)  
            n_positive_numbers += 1
            average = sum(positive_numbers) / len(positive_numbers)
    
    print(f"{n_positive_numbers} valores positivos")
    print(f"{average:.1f}")  

positives_and_average()