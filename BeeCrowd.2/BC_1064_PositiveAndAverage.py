'''

def positives_and_average():
    positive_numbers = []  

    for _ in range(1, 7):
        number = float(input( ))

        if number > 0:
            positive_numbers.append(number)  

    total_positives = len(positive_numbers)  

    if total_positives > 0:
        average = sum(positive_numbers) / total_positives
        print(total_positives)
        print(f"{average:.2f}")  
    else:
        print("Nenhum número positivo foi digitado.")

positives_and_average()
'''

def positives_and_average():
   
    positive_numbers = 0  
    numeros = []

    for n in range (1, 7):
        n = float(input( ))
        numeros.append(n)
        average = sum(numeros)/6

        if n > 0:
            positive_numbers += 1  

    print(positive_numbers)
    print(f"{average:.2f}")  

positives_and_average()