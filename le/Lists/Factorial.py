# Fred Wang 11/28/2017

def factorial():
    """
    This function takes in a number and finds the factorial for it
    factorial: finds all the smaller number and multiplies all of them together with the original number
    """
    number = int(input("Your number: "))
    # This takes in the number

    for num in range(1,number):
        # This runs the program through all the possible smaller whole numbers
        number = number * num
        # This multiplies and adds the result to your number so it could be repeated
    print(number)