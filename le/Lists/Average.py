# Fred Wang 11/28/2017

def average():
    """
    This function takes in 4 inputs and averages them
    """
    grade = []
    # This is the list that will take in the grades of the student
    for grades in range(0,4):
        # This allows the program to repeatedly take 4 inputs
        while True:
            # This loops asks for an input again if the input was an alphabet
            try:
                # This is to test if the input is an alphabet
                each_grade = float(input("In put the grade of the student: "))
                # This takes in the input
                grade.append(each_grade)
                # This adds the number into the list
                break
            except:
                print("You have inputted a character, please input a number and try again")
                # This is a fall back if the input is a character, this also lets the loop continue to ask for a number
                # until it receives it

    def calculate_average():
        """
        This function takes the first 4 numbers in the list and find the average of it
        """
        print(grade)
        # This prints the grades in the list
        average = (grade[0] + grade[1] + grade[2] + grade[3]) / 4
        # This calculates the averages
        print(average)
        # This prints the average

    calculate_average()