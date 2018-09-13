def multiplication_table():
    """
    Write a program to create a multiplication table
    for a given user input.The table should include its multiples from 1 to 10

    * I added a function that allows the user to select the multipliers instead of just 1 to 10
    """
    user_input = input("Input the number you wanted listed in a multiplication table: ")
    first_range_input = int(input("Input the range of multipliers you want shown, enter 0 for default; 1: "))
    second_range_input = int(input("Input range of multipliers you want shown, enter 0 for default; 10 "))

    if first_range_input == 0:
        first_range_input = 1
    # This sets the range of the multiplier to 1 if 0(default) is entered
    else:
        first_range_input = first_range_input

    if second_range_input == 0:
        second_range_input = 10
    # This sets the range of the multiplier to 10 if 0(default) is entered
    else:
        second_range_input = second_range_input

    try:
        for num in range(first_range_input, second_range_input + 1):
            print(str(user_input) + " x " + str(num) + " = ", int(num) * int(user_input))
    except:
        for num in range(first_range_input, second_range_input):
            print(str(user_input) + " x " + str(num) + " = ", int(num) * float(user_input))
    # Try and except was added due to this possibility of decimals, first line of code removes and ignores decimals
