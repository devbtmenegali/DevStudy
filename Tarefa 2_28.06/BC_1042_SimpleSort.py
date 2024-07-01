
x, y, z = map(int, input().split())

numbers = [x, y, z]

numbers.sort()              # Ordem crescente
for num in numbers:
    print(num)              # Imprime cada número em uma linha

print()                     # Adiciona uma linha em branco para separar as listas

print(x)
print(y)
print(z)