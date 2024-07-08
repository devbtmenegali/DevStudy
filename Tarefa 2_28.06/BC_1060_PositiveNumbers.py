
positivos = 0

for _ in range (6):
    numero = float(input())
    if numero > 0:
        positivos += 1

print(f"{positivos} valores positivos")
