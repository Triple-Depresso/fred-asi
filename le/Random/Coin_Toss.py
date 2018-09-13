#  Fred Wang 12/7/2017

history = []
last_flip = []
points = {"Points":0}

while True:
    # This is here to continuously asks for a valid input
    print("----------------------------------------------------------------------")
    menu_input = input("Please input an action, input 'Help' for the options: ").lower()
    # Takes in the input of the user's choice of actions

    def display():
        """
        This function displays the history of the coin flip, what the last flip was, and the total points
        """
        print("History of the flips: ", history)
        print("Results of last flip: ", last_flip)
        print("Total points: ", points["Points"])

    def help():
        """
        Displays the available actions/commands
        """
        print("Display - Displays the current score")
        print("Flip ---- Flips the coin according to amount of times inputted")
        print("Help ---- Displays the options")
        print("Exit ---- Exits the program")

    def times_flip():
        while True:
            # This is here to continuously asks for a valid input
            try:
                times = int(input("Input the amount of times you want to flip the coin: "))
                # This takes in the number of flips as a number
                # ------------------------------------------
                # This if/else statement here is to display different messages if the user inputs a 0
                if times != 0:
                    return times
                else:
                    print("Coin has been flipped 0 times")
                    return times
            except:
                print("Please input a number, not text")
                # This is shown when the user does not input a number

    def record():
        """
        record() -> ['Heads', 'Heads', 'Tails', 'Heads']

        This functions gives an amount of random heads or tails based on the user input from times_flip()
        """
        import random
        times = 0
        # This resets the times flip if there is memory left from the last time it ran
        times = times_flip()
        # This gets a new number(For times to flip the coin) from the user
        last_flip = []
        # This resets the history of the last result
        side = ["Heads", "Tails"]
        # This is all the possible sides that the coin can land on
        if times != 0:
            # The function below will only activate if the times flip is not 0
            for num in range(1, times + 1):
                # This flips the coin according the the times flip
                flip = random.choice(side)
                last_flip.append(flip)
                # This stores the result of the flip
        print(last_flip)
        # This displays the result of the current flip
        return last_flip

    if menu_input == "display":
        display()
        # Activates the display command

    elif menu_input == "help":
        help()
        # Activates the help command

    elif menu_input == "exit":
        exit()
        # Exits the program

    elif menu_input == "flip":
        """ 
        This activates the main function, flipping the coin
        """
        recent_flip = record()
        # This stores the result of the current flip
        length = len(recent_flip)
        # This gets the length of the last flip. Aka. the times flip
        last_flip = []
        # This stores the result of the last flip
        round_points = 0
        # This is the point of the current round
        for num in range(0, length):
            # This runs the program according the the times the coin hsa been flipped
            history.append(recent_flip[num])
            # This add each result of the coin flip to the history
            last_flip.append(recent_flip[num])
            # This adds the result of the current coin flip to the 'last flip history'
            if recent_flip[num] == "Heads":
                # Below activates if the coin lands on heads
                points["Points"] += 1
                # This adds 1 to the total point if the coin lands on heads
                round_points += 1
                # This adds 1 to the current round points
            elif recent_flip[num] == "Tails":
                # Below activates if the coin lands on tails
                points["Points"] -= 1
                # This subtracts 1 to the total point if the coin lands on tails
                round_points -= 1
                # This subtracts 1 to the current round points if the coin lands on tails
        print("You got: {} points!".format(round_points))
        # This shows how many point the player got on that specific round, using the round_points
    else:
        print("Please input a valid option")
        # prints this message if the user does not input something valid
