def sum_odd_nunmbers():

    X = int(input())
    Y = int(input())
    odd_numbers = []

    if X > Y:
        X, Y = Y, X

    for number in range(X, Y):
        if number % 2 == 1:
            odd_numbers.append(number)

    result = sum(odd_numbers)
    print(result)

sum_odd_nunmbers()