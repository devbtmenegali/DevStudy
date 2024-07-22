X = int(input())
Y = int(input())

if X > Y:
    X, Y = Y, X  

odd_sum = 0

for num in range(X + 1, Y):  
    if num % 2 != 0:  
        odd_sum += num  

print(odd_sum)