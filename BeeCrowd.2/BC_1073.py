N = int(input())

if 5 < N < 2000:
    for i in range(2, N + 1, 2):  
        print(f"{i}^2 = {i**2}")  
else:
    print("Entrada inválida. N necessita ser entre 5 a 2000.")