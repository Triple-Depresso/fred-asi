# Fred Wang 12/7/2017
# Not sorry

names = []
# List of names for the player
name_list_wins = {}
# Numbers of wins for each player
name_list_tries = {}
# Number of tries for each player
name_list_wagers = {"pool": 0}
# The wager each player places
wager_on_off = False
# This is a wager on/off switch


def num_players():
    """
    This function takes in and records the number of players
    """
    while True:
        # This is here so it asks repeatedly for a number if the user inputs text
        # you will see this this usage many times after, this is to prevent people from breaking the program
        try:
            num = int(input("Please input the amount of players: "))
            return num
        except:
            print("Please input a number, not text.")
players = num_players()


def player_name():
    """
    This function takes in and records the names so they can be displayed in wins, loses, and their wagers
    """
    for num in range(1, players + 1):
        # This asks for names repeatedly according to the number of players
        name = input("Please input the player name here: ")
        # This takes in the names
        # --------------------------------------------------------------------------
        # Below places the names in the correct category, ex. wins
        names.append(name)
        name_list_wins[name] = 0
        name_list_tries[name] = 0
        name_list_wagers[name] = 0
player_name()


while True:
    # This is here to continuously asks for a valid input
    print("------------------------------------------")
    menu_action = input("Please input an action, input 'Help' for the list of options: ").lower()
    # This asks for the user's choice of action


    def help():
        """
        This function tells the user what commands/actions are available
        """
        print("------------------------------------------")
        print("These are the actions available")
        print("")
        print("Display -- Displays the current score board")
        print("Help ----- Displays the options available")
        print("Start ---- Starts the game")
        print("Settings - Sets the difficulty, the range of numbers you have to guess from")
        print("Wagers --- Add wagers to the game")
        print("Exit ----- Exits the program")


    def wager_explain():
        """
        This further explains what wagers are and how it works
        """
        print("------------------------------------------")
        print("The wager system is winner takes all")
        print("Everyone input their amount of wager, and whoever guesses the right number")
        print("Receives all the money that was placed")


    def wagers():
        """
        This function takes in and records every player's wagers
        """
        for num in range(0, len(names)):
            # This runs the program according to how many players there are
            while True:
                # This is here to continuously asks for a valid input
                name = names[num]
                # This takes a name from the player list
                try:
                    amount = int(input("Please indicate the amount {} want to bet: ".format(name)))
                    # Takes in the user's amount of wager. The name is inserted with the name taken from the player list
                    name_list_wagers[name] = amount
                    # Adds to the wager to the wager list
                    break
                except:
                    print("Please input an amount")
                    # Asks for a valid input

    # --------------------------------------------------------------------------------------------------------------
    # This is placed here specifically before every other 'command activator' is because this will activate other
    # commands down the line
    # Command activators: These are the codes that calls another actions when a specific word is entered into the prompt
    if menu_action == "wagers":
        # This activaes only when the user calls it
        if wager_on_off == False:
            # This following command only activates when wagers are not activated
            while True:
                # This is here to continuously asks for a valid input
                y_n = input("Would you like to activate wagers? y/n - Input 'Explain' to go in detail: ").lower()
                # This asks if the user wants to activate wagers
                if y_n == "explain":
                    # This explains how the wager works
                    wager_explain()
                elif y_n == "y":
                    # This turns on the wager
                    wager_on_off = True
                    wagers()
                    break
                elif y_n == "n":
                    # This cancels the wager
                    print("Canceled")
                    break
        else:
            wagers()
            # This is to go strait to editing the wagers if wagers were ALREADY activated


    def display():
        """
        Shows the player names, amount won and lost
        and the wager everyone placed IF AND ONLY if wagers are activated
        """
        print("------------------------------------------")
        print("Player's names: ", names)
        print("Amount everyone has won: ", name_list_wins)
        print("Amount everyone has failed: ", name_list_tries)
        if wager_on_off == True:
            # This is to see if the wager is turned on, prints the wager only if wagers are turned on
            print("Wagers everyone has placed: ", name_list_wagers)


    def lvl_difficulty():
        """
        This is settings for the game, it ca determine the difficulty, which is the range of numbers that
        the code can pick from, default 1 - 10
        """
        print("Please input the difficulty here - Easy/Medium/Hard/Custom")
        print("Or input 'spec' here to see the number range of each")

        while True:
            # This is here to continuously asks for a valid input
            level = input("Difficulty: ").lower()
            # -----------------------------------------------------------------------
            # Below are the command activators, sets the difficulty
            if level == "easy":
                # Sets to 1 - 10
                num_range = [1, 10]
                return num_range
            elif level == "medium":
                # Sets to 1 - 20
                num_range = [1, 20]
                return num_range
            elif level == "hard":
                # Sets to 1 - 30
                num_range = [1, 30]
                return num_range

            elif level == "custom":
                # allows the user to set a custom range
                anger = 0
                while True:
                    # This is here to continuously asks for a valid input
                    try:
                        # Below takes the range and stores it
                        num1_range = int(input("input the first number of the range: "))
                        num2_range = int(input("Input the last number of your range: "))
                        num_range = [num1_range, num2_range]
                        return num_range
                    except:
                        print("Please input a number, not text, thank you.")
                        # This message is printed if the user doesnt enter a valid number
                        anger += 1
                        if anger == 3:
                            print("You tried to break this code 3 times, like common, its not gonna work.")
                        # Easter egg

            elif level == "spec":
                # Tells the user what the range of each difficulty is
                print("------------------------------------------")
                print("Easy   = 1 - 10 - Default\nMedium = 1 - 20\nHard   = 1 - 30\nCustom = Set your own range")
            else:
                print("Please check your spelling and try again")
                # This prints out if the user does not input a valid answer

    # --------------------------------------------------------------------------------------------
    # Below is another command activator, placed before the others because it affects the range of the number selection
    # Aka. effects something down the line
    if menu_action == "settings":
        difficulty = lvl_difficulty()


    def user_guess():
        """
        This takes in each player's guesses
        """
        user_list = {}
        # Used so this function can return multiple answer
        for num in range(0, players):
            # This asks for each player's guesses
            user_name = names[num]
            # This takes a name from the name list
            while True:
                # This is here to continuously asks for a valid input
                try:
                    user_choice = int(input("Input {}'s choice of number here: ".format(user_name)))
                    # This takes in the user choice
                    if user_choice not in user_list:
                        # This check if someone has already guessed the number
                        user_list[user_choice] = user_name
                        # stores the choice of number if it's not taken
                        break
                    else:
                        print("{} already choose this number".format(user_list[user_choice]))
                        print("Please input another number and try again.")
                except:
                    print("Please input a number, not text.")
        print(user_list)
        return user_list


    def rand_num():
        """
        Used to find the Magic Number
        """
        import random
        try:
            num = random.randint(difficulty[0], difficulty[1])
            # This gets the random number using the range provided by lvl_difficulty()
            return num
        except:
            num = random.randint(1, 10)
            # This is the defualt range
            return num


    def start():
        """
        Start() -> {"Won", "name"}
        Start() -> {"Lost", {name:his/her guess, name:his/her guess, name:his/her guess...}

        Main action, tests for if anyone got the random number right

        This function exports a list, this is used as the functions needs to export 2 or more results
        The function's list's first item will always be if someone won or not, and the second/following will be who won
        """
        num = rand_num()
        # This takes the random number and store it
        guess = user_guess()
        # This takes the player's guesses and store it
        if num in guess:
            # This checks if anyone's guesses is the random number
            # Activates the following code if someone got the number right
            print(guess[num], " Won!!")
            print("The correct number is: ", num)
            # guess[num] in this case is the same as the person whom just got the right answer
            name_win_lost = ['Won', guess[num]]
            # This is used so the function can export multiple results, the first being if the user won and the second
            # being who won
            return name_win_lost
        elif num not in guess:
            # This is when no one got the number right
            print("No one got it right")
            print("The correct number was: ", num)
            name_win_lost = ["Lost", guess]
            # Similar to the upper section, this is used to export the names of the people that lost and indicating
            # that no one got the number right
            return name_win_lost

    # ------------------------------------------------------------------------
    # The following are command activators

    if menu_action == "display":
        display()
        # Actives the display command

    elif menu_action == "help":
        help()
        # Actives the help command

    elif menu_action == "exit":
        exit()
        # Actives the help command

    elif menu_action == "start":
        # Activates the main/start function
        win_lost_name = start()
        # This stores the result of the main/start function
        win_lost = win_lost_name[0]
        # win_lost_names[0] is if someone won or not
        winner = win_lost_name[1]
        # win_lost_name[1] is the name of the player who got the number right

        if win_lost == "Won":
            # win_lost_name[1] is the name of winner
            name_list_wins[winner] += 1
            # This adds a win for the winner
            for num in range(0, len(names)):
                name_list_tries[names[num]] += 1
                # This adds a try to everyone's names including the winner's name
            name_list_tries[winner] -= 1
            # This removes the try from ONLY the winner
        elif win_lost == "Lost":
            for num in range(0, len(names)):
                name_list_tries[names[num]] += 1

        if wager_on_off == True:
            # This is the section that calculates the wager IF AND ONLY IF wagers are turned on
            total_wage = 0
            # Resets the total wage for the current round
            for num in range(0, len(names)):
                # This gives the total of everyone's wages by adding them all up
                total_wage = total_wage + name_list_wagers[names[num]]
            total_wage += name_list_wagers["pool"]
            # This add the pool onto the total wage too, pools are created if no-one got the number right but still
            # placed a wager
            for num in range(0,len(names)):
                name_list_wagers[names[num]] = 0
                # This clears everyone's wagers if there is a winner
            if win_lost == "Won":
                name_list_wagers[winner] = total_wage
                # This gives everyone's and the pooled wagers to the winner
            else:
                name_list_wagers["pool"] = total_wage
                # This pools the wagers if no one won
