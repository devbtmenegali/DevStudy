def six_odd_numbers ():

    enter_number = int(input())

    for number in range (enter_number,enter_number + 12):
        if number % 2 == 1:
            
            print(number)

six_odd_numbers()