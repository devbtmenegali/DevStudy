N = int(input())

in_range = 0
out_of_range = 0

for _ in range(N):
    X = int(input())
    if 10 <= X <= 20:
        in_range += 1
    else:
        out_of_range += 1

print(f"{in_range} in:")
print(f"{out_of_range} out:")