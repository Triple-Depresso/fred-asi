# Fred Wang Sept 18 2018

"""
Write a program that prints the sum of the numbers in S,
where S is a string that contains a sequence of numeric characters separated by commas.
For example, if  S = “1, 4, 2”,  the sum of S would be 7

upgrade - asks the user for the numbers within S
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
            print("Please enter a number: ")


def is_num(x):
    return type(x) == int

def ask_for_num():
    """
    this function asks the user for number inputs and compiles it into a list
    """
    s = ""
    while 1:
        data = input("Enter a number or 'stop': ").lower()

        if data == "stop":
            # tests for if the user wants to stop inputting numbers
            return s

        else:
            try:
                # try and except use as a simple version of, if s.is_a_number() == true
                # used this cus im lazy
                int(data)
                s += data
                s += ","
            except ValueError:
                # rejects the input if it's not a number
                print("Please enter a number")

def add_sum(s):
    """
    THis function adds up all the numbers within a string separated my " , "

    add_num("22,123") ---> 145
    """
    final = 0
    # the sum
    num_list = s.split(",")
    # turns the numbers into a list
    del num_list[-1]
    # deletes the last space - not needed

    print("your numbers: ", num_list)
    #shows your list

    for count in range(len(num_list)):
        final += int(num_list[count])
        # adds up all the numbers

    return final

while 1:
    # infi loop that allows the program to be reused
    print("-----------------------------")
    print(add_sum(ask_for_num()))
    # starts the program
