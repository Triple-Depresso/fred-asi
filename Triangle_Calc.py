# Fred Wang Sept 6th 2018
# Bored

"""
Write a program in Python that calculates the area of a triangle.
Documentation: include a header and in-line comments
"""

def get_measure():
    """
    This function asks the user for inputs on the base and height of the triangle
    """
    while 1:
        # while 1 provides a infi loop that repeatedly asks the the user for a valid input
        try:
            # acts like a control flow(if statement) that tests if the inputted data is a number
            base = int(input("input the base of triangle here: "))
            break
        except ValueError:
            # the result if the inputted data is not a number
            print("Please enter a number")

    while 1:
        # while 1 provides a infi loop that repeatedly asks the the user for a valid input
        try:
            # acts like a control flow(if statement) that tests if the inputted data is a number
            height = int(input("input the height of the triangle here: "))
            break
        except ValueError:
            # the result if the inputted data is not a number
            print("Please enter a number")

    return base, height
    # output the data as a list

while 1:
    print("----------------------------------------------")
    print("This program calculates the area of a triangle")

    measure = get_measure()
    # runs the function and get the user input as a list

    print("The area of your triangle is:\n" + str((measure[0] * measure[1]) / 2))
    # measure[0], measure[1] unpacks the list
    # using + and str() instead of , removes the space before the number
