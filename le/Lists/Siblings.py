# Fred Wang 11/28/2017

# I apologize for adding in so much unnecessary features, Aka. more for you to mark, but I got bored and I wanted
# to make fun of EA

print("NOTICE! This program only takes in a maximum of 5 names")
print("For more storage space, please go to our website and buy the 'Storage' DLC pack, officially supported by EA")

while True:
    # Used for so the program would ask for what the user wants until the user inputs a viable option
    options = input("Please input the action you want performed, input 'Help' for the options: ")
    options = options.lower()

    def DLC_key():
        """
        This function is for activation of the DLC 'Storage expansion'
        it tests for if the key is right for the DLC and activate it if it is correct
        """
        while True:
            # This continuously asks for a right DLC Key until the user inputs "Exit" or the right Key
            key = input("Please input the DLC key here or type Exit to cancel: ")
            # This takes in the key
            if key == "GGEZ":
                # This tests for is the key is right
                print("Key Successfully verified!")
                return True
            elif key == "Exit":
                # This exits the function and returns the user to the main menu
                break
            else:
                print("Key is incorrect or already in use, please check your input and try again")

    def purchase():
        """
        This function simulates a purchase of the DLC pack taking in the user's credit card number and date
        the credit card and date is never actually used, instead a delay is added in between to simulate the loading
        or processing time
        """
        import time
        # This is used so a delay can be created in this function
        while True:
            # This is used so that the program would continuously ask for y or n if the user didn't input either
            yn = input("Welcome to the purchase page, would you like to purchase the storage expansion pack? y/n: ")
            # This takes makes sure if the user wants to buy the DLC and asks them yes or no
            if yn == "y":
                # Below are the functions that simulates a transaction
                # ----------------------------------------------------
                print("Loading...")
                time.sleep(2)
                cd_num = input("Please enter your master card number: ")
                cd_date = input("Please enter your master card date: ")
                print("Please wait while we process your card")
                time.sleep(4)
                print("Card accepted! Generating your DLC Key...")
                time.sleep(4)
                print("Your Storage expansion pack key is: GGEZ \nPlease write this down or take a photo")
                # ----------------------------------------------------
                break
            elif yn == "n":
                # This is to cancel if the user inputs n
                print("Canceling...")
                time.sleep(2)
                break
            else:
                # This is if the user inputs something other than y or n
                print("Error!! Please Try again!")


    # This is to test if the DLC has been activated
    # It is placed before everything else because some code needs the DLC as a reference
    # So the program has to run this first
    if options == "DLC Key":
        # This activates the DLC function if the user choose to
        DLC_storage = DLC_key()


    def help():
        """
        This function prints and format out all the help options
        """
        print("------------------------------")
        print("These are the actions possible")
        print("                              ")
        print("Create ---- Create name list")
        print("DLC Key --- Input your DLC key to expand storage")
        print("Help ------ Command options")
        print("Purchase -- Purchase the DLC directly through this program")
        print("Exit ------ Exits the program")

    def name_list():
        """
        This is the main function which creates and stores all the names
        """
        # This is the storage space for all the names
        # -------------------------------------------
        name1 = None
        name2 = None
        name3 = None
        name4 = None
        name5 = None
        name_6 = None
        name_7 = None
        name_8 = None
        name_9 = None
        name_10 = None
        list = ()
        # storage space with _ means it's part of the DLC pack (6-10)
        # -------------------------------------------

        while True:
            try:
                # HD_names stands for Hard Drive for names
                # This tests if the DLC has been activated, if it has, then the storage space will turn to 10
                if DLC_storage == True:
                    HD_names = 10
            except:
                # This defaults to 5 if the DLC has not been avtivated
                HD_names = 5

            for names in range(0,HD_names):
                # This runs the program 5 or 10 times depending on if the DLC has been activated
                print("Names inputted: ", names)
                print("Storage space for names left: ", HD_names - names)
                intake = str(input("Input the names here or enter 'Stop' to stop the program: "))
                # This is the intake of the names
                if intake == "Stop":
                    # This stops the program if the user inputs exit
                    break
                else:
                    # Below are the functions that puts the names in the storage spaces
                    # -----------------------------------------------------------------
                    if names == 0:
                        name1 = intake
                    elif names == 1:
                        name2 = intake
                    elif names == 2:
                        name3 = intake
                    elif names == 3:
                        name4 = intake
                    elif names == 4:
                        name5 = intake
                    if names == 5:
                        name_6 = intake
                    if names == 6:
                        name_7 = intake
                    if names == 7:
                        name_8 = intake
                    if names == 8:
                        name_9 = intake
                    if names == 9:
                        name_10 = intake
                    # ----------------------------------------------------------------

            # Below are the functions that puts what's in the storage spaces into a list for the user to view
            # -----------------------------------------------------------------------------------------------
            if name1 == None:
                print("input something")
            elif name2 == None:
                list = (name1)
                print(list)
                break
            elif name3 == None:
                list = (name1, name2)
                print(list)
                break
            elif name4 == None:
                list = (name1, name2, name3)
                print(list)
                break
            elif name5 == None:
                list = (name1, name2, name3, name4)
                print(list)
                break
            elif name_6 == None:
                list = (name1, name2, name3, name4,name5)
                print(list)
                break
            elif name_7 == None:
                list = (name1, name2, name3, name4, name5, name_6)
                print(list)
                break
            elif name_8 == None:
                list = (name1, name2, name3, name4, name5, name_6, name_7)
                print(list)
                break
            elif name_9 == None:
                list = (name1, name2, name3, name4, name5, name_6, name_7, name_8)
                print(list)
                break
            elif name_10 == None:
                list = (name1, name2, name3, name4, name5, name_6, name_7, name_8, name_9)
                print(list)
                break
            else:
                list = (name1, name2, name3, name4, name5, name_6, name_7, name_8, name_9, name_10)
                print(list)
                break
            # ----------------------------------------------------------------------------------------------

    # These are to activate the functions that the user inputted
    # ------------------------------------------------------------
    if options == "create":
        # Activates the create list function, Aka. main function
        name_list()
    elif options == "help":
        # Activates the Help function, shows all the available options
        help()
    elif options == "purchase":
        # Activates the Purchase function, simulates a purchase for the DLC Key
        purchase()
    elif options == "exit":
        # Exits the program
        exit()