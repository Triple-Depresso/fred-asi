def sum_average():
    """
    Write a program to calculate the sum and average of a set of numbers.
    If you input 0, the program closes.
    """
    print("Input a value, input 0 to exit:")

    first_input = int(input())
    if first_input != 0:
        loop_stopper = True
    # This is to test if the first number is 0
    else:
        loop_stopper = False
        print("Sum of numbers: 0")
        print("Average of numbers: 0")
    # This is to run the command if the first number inputted is not 0

    while loop_stopper is True:
        for loop_count in range(1, 9999999999):
            # This is to run and count how many loops was ran,
            # Aka. the number that can be used to divide by when it comes to averaging
            second_input = int(input())
            if second_input == 0:
                print("Sum of numbers: " + str(first_input))
                calculate_average = first_input / loop_count
                print("Average of numbers: " + str(calculate_average))
                break
                # This is to test if 0 was entered and stop the process of asking for data
                # This also calculates the average
            else:
                first_input += second_input
                # This adds newly entered number into the data base
                # Aka. the sum of the numbers entered
        break
