# Fred Wang 11/28/2017

def character_counter():
    '''
    This function takes in a series of text and characters and it counts the amount of each characters
    '''

    org_text = input("Please input your text: ")
    # This takes in the input from the user
    list = {}
    # This is the main list

    for counter in range(0, len(org_text)):
        # This runs so that ever alphabet in the given text is tested
        character = org_text[counter]
        # This singles out the specific character
        if character in list:
            # This checks if the specific character is already in the list
            list[character] += 1
            # This adds to the character counter if the character is already in the list
        else:
            list[character] = 1
            # This creates a new character in the list if it did not exist before

    print(list)