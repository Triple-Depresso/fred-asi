def word_check():
    """
    Write a program that checks for the word “monkey”. Your checker will first ask for a the word “monkey”, then
    repetitively ask the user to check the word. When the user types the same word, acknowledge that the right word was
    provided. Do this WITHOUT if statements.
    """
    org_word = input("What is your word: ")
    test_word = input
    while test_word != org_word:
        # This tests for if the 2 inputted values are the same WITHOUT using if (and try)
        print("Check your word:")
        test_word = input()
        # This asks for a new input for the user to try again
    print("Correct!")
