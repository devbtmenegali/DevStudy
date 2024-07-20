
def even_numbers():

    even = 0

    for _ in range(5):
        numbers = int(input())
        
        if numbers % 2 == 0:
            even += 1

    print(f"{even} valores pares")

even_numbers()