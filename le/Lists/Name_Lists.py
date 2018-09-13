# Fred Wang 11/28/2017

list = []
# This is the main list of names


def get_names():
    """
    This function takes in the first 5 names as a text input and store it in the list
    """
    for num_name in range(1, 6):
        # This is a loop that takes the first 5 names
        first_name = str(input("Input the names here: "))
        # This takes in the names
        list.append(first_name)
        # This adds the names to the list
get_names()


while True:
    def adding_names():
        """
        This function takes a name and add it to the list of names
        """
        add_name = input("Please input the name you want added: ")
        # This takes in the new name
        list.append(add_name)
        # This stores the new name in the list


    def display():
        """
        This presents the list to the user
        """
        print(list)


    def remove_name():
        """
        This takes a specified name and remove it from the list
        """
        del_name = str(input("Input the name you want deleted: "))
        # This takes in the name that the user wants removed
        if del_name in list:
            #This checks if the name is even in the list
            for list_index in range(0, len(list)):
                # This runs though all the words to give each word in the list an index number
                if del_name == list[list_index - len(list)]:
                    # This checks if each word corresponds to the word that wants to be deleted
                    del list[list_index]
                    # This deletes the word using the index number that corresponds
        else:
            print("Please check your spelling including caps, if you've made sure you've inputted the right word, then the"
                  "word do not exist within the list")
            # This is a fall back result if the user spelled the name wrong, capitalized it wrong, or inputted a word that
            # does not exist within the list


    def edit_name():
        """
        This function takes an input of the word in the list and replaces it with a new word
        """
        be_edited = input("Input which name you want edited: ")
        # This takes in the word that wants to be replaced
        new_word = input("input the new name: ")
        # This takes in the new word that will replace the old word
        if be_edited in list:
            # This checks if the word that wants to be replaced is in the list
            for list_index in range(0, len(list)):
                # This assigns an index number that corresponds to each word in the list
                if be_edited == list[list_index]:
                    # This checks which word is the word that wants to be replaced
                    del list[list_index]
                    # This deletes the word so it can be replaced using the index number received earlier
                    list.insert(list_index, new_word)
                    # This adds the new word where the old word was deleted, this also uses the index number like mentioned
                    # above
                else:
                    pass
                    # This allows the loop to check the next word
        else:
            print("Please check your spelling including caps, if you've made sure you've inputted the right word, then the"
                  "word do not exist within the list")
            # This is a fall back in the case of user inputting the wrong word, spelling or capitalization for the word that
            # wants to be replaced


    def help():
        # This displayes the help menu and the possible actions
        print("")
        print("The actions possible are the following")
        print("")
        print("- Display names -- This shows the list")
        print("- Add names     -- This lets you add to the list")
        print("- Remove names  -- This lets you remove any names on the list")
        print("- Edit names    -- This lets you edit any names on the list")
        print("- Exit          -- This exits and closes the program")
        print(" ---------------------------------- ")

    # ---------------------------------------------------------
    # This section asks for what action the user wants to take
    action = input("Please indicate which action you want to take, type 'help' to see the actions: ")
    if action == "Help":
        help()
    elif action == "Display names":
        display()
    elif action == "Add names":
        adding_names()
    elif action == "Remove names":
        remove_name()
    elif action == "Edit names":
        edit_name()
    elif action == "Exit":
        exit()

    # -----------------------------------------------
    # This section is to have the program work even if the user typed in commands with lower case
    elif action == "help":
        help()
    elif action == "display names":
        display()
    elif action == "add names":
        adding_names()
    elif action == "remove names":
        remove_name()
    elif action == "edit names":
        edit_name()
    elif action == "exit":
        exit()
    else:
        print("Please check your spelling and try again")