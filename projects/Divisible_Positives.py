# Fred Wang Sept 18 2018

"""
Write a program that looks for the first positive integer that is divisible by both 11 and 12

upgrade - instead of 11 and 12, the program asks for a user number input
"""

def ip_input(prt):
    """
    ip_input - idiot proof input
    this function is an add-on to the normal input() function
    it checks and makes sure the input is an integer, does not accept the input if the input is not an integer
    """
    while 1:
        try:
            x = int(input(prt))
            return x
        except ValueError:
            print("Please enter a number")

while 1:
    # infi loop that allows the program to be reused
    print("-------------------------------------")

    first = ip_input("Input your first number: ")
    second = ip_input("Input your second number: ")
    # asks the user for number inputs

    counter = 0
    # loop counter

    print("Please wait for the program to finish - this might take a while depending on your numbers")
    while 1:
        # continue to find the next positive full num
        counter += 1
        # keeps track of the number

        if counter % first == 0 and counter % second == 0:
            # tests if the new number is divisible

            print("The number: ", counter, "\nIs divisible by both: ", first, "and", second)
            # outputs the number
            break
