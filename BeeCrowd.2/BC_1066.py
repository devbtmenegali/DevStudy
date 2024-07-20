def even_numbers():

    even = 0
    odd = 0 
    positive = 0
    negative = 0

    for _ in range(5):
        numbers = int(input())
        
        if numbers % 2 == 0:
            even += 1
        elif numbers % 2 == 1:
            odd += 1
        if numbers > 0:
            positive += 1
        elif numbers < 0:
            negative += 1

    print(f"{even} valor(es) par(es)")
    print(f"{odd} valor(es) impar(es)")
    print(f"{positive} valor(es) positivo(s)")
    print(f"{negative} valor(es) negativos)")

even_numbers()