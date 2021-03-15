from time import *

timeStart = time()  # This part will calculate the time.
question1 = ("What\'s 12+6? ")
question2 = ("What city do The Beatles come from? ")
question3 = ("Where was the first modern Olympic Games held? ")
question4 = ("When did the French revolution began? ")
question5 = ("How many people lives in Iceland? ")
question6 = ("How many elements are there in the periodic table? ")
question7 = ("Until 1923, what was the Turkish city of Istanbul called? ")
question8 = ("When was Netflix founded? ")
question9 = ("When was Atatürk born?")
question10 = ("In what year did the Western Roman Empire come to an end?")
questions = [question1, question2, question3, question4, question5, question6, question7, question8, question9,
             question10, ]

answer1 = ("18")
answer2 = ("Liverpool")
answer3 = ("Athens")
answer4 = ("1789")
answer5 = ("364134")
answer6 = ("118 ")
answer7 = ("Constantinople")
answer8 = ("1997")
answer9 = ("1938")
answer10 = ("476")
answers = [answer1, answer2, answer3, answer4, answer5, answer6, answer7, answer8, answer9, answer10]

# Game Settings

points = 0
name = None
yes = ['Yes', 'yes', 'YES']
no = ['No', 'no', 'NO']


# Reset

def game_reset():
    '''
    This function resets all variables of the whole game for a new play
    '''

    global points
    global name
    global age
    points = 0
    name = None


def game_intro():
    '''
    This function welcomes the player and asks him if he is ready .
    '''

    print("\n       ------ !! Welcome to the QuizGame !! ------\n")
    global name

    while name == None:
        name = input("What's your name? ")
        correct = input("Are you ready? ")
        rules = input("Do you want to see the rules? yes/no: ")

        if yes.count(rules) == True:
            print(rules)
            print("")
            print("This is a knowledge competition!")
            print("There will be ten questions ")
            print("Each question will be worth 10 points")
            print("If you answer 5 questions wrong you will loose")
            print("Don't forget that City names must start with a capital letter")
            print("Good luck and enjoy the game!")
        else:
                 print("Don't forget that City names must start with a capital letter")

        if yes.count(correct) == True:  ##"Yes" or ok == "yes" or ok == "YES":
            print("let's go on!", name)

        else:

            print("Okay you can restart whenever you ready")
            name = None


def print_play_status(x):
    global points
    print("Currently your total points are", points)
    print("Challenge", x + 1, "\n")


def play_quest(x):
    '''
    This functions asks the player question X, checks if player's answer is right and eventually changes the variable points.
    '''

    global points
    answerPlayer = input(questions[x])
    if answerPlayer == answers[x]:
        print("Well done,", name + ", 10 points gained! Let's move to the next question.\n")
        points += 10
    else:
        print("Wrong! 0 points gained, the correct answer was:", answers[x], ". Next question...\n")


def game_play():
    '''
    This function tells the player his current score and the current challenge number
    and play_quest-function how many and which questions it must asks the player.
    '''

    for x in range(len(questions)):
        print_play_status(x)
        play_quest(x)


def game_end():
    """"
     This function.
     tells the player his finish score.
     asks the player if wants to play again.
     says if the player won or lost
    """
    timeFinsh = time()
    totalTimeToAnswer = timeFinsh - timeStart
    print("You took", totalTimeToAnswer, "seconds to answer all the questions.")

    print("\nYou finished the game with a total of", points, "points! \n")
    if points <= 50:
        print("Unfortunately you lost the game (LOOOOSER)")
    else:
        print("Congrats YOU WON!!! Your reward is a one week trip to North Korea")

    again = None

    while again == None:
        again = input("Once again? ")
        if yes.count(again) == True:
            print("\n!!Enjoy the game!!\n")
            game_control()
        elif no.count(again) == True:

            print("                             Thanks for your participation!")
            print("                           ------ !! bye !! ------")
        else:
            print("just yes or no!")
            again = None


def game_control():
    game_reset()
    game_intro()
    game_play()
    game_end()


game_control()