def num_tower():
    """
    Write a program to create the following pattern:

    1
    22
    333
    4444
    55555
    666666
    7777777
    88888888
    999999999
    """
    for num in range(1, 10):
        print(str(num) * num)
    # Print out the number as a string and stack it up according to its own value
