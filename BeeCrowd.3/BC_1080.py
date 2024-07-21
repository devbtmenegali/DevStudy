def highest_and_position():

    numbers = []

    for i in range(100):
        i = int(input())
        numbers.append(i)

    highest = max(numbers)
    position = numbers.index(highest)

    print(highest)
    print(position)

highest_and_position()