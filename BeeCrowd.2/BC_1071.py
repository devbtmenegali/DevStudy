def sum_odd_nunmbers():

    number1 = int(input())
    number2 = int(input())

    odd_numbers = []

    for number in range(number1, number2 + 1):
        if number % 2 == 1:
            odd_numbers.append(number)

    result = sum(odd_numbers)
    print(result)

sum_odd_nunmbers()