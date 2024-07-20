def odd_numbers ():

    enter_number = int(input())

    for number in range (1,enter_number + 1):
        if number % 2 == 1:
            
            print(number)

odd_numbers()