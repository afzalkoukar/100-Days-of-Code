import random
from art import logo



EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

def set_difficulty():
    level = input("type e for Easy mode or h for hard mode\n")

    if level =="e":
        return EASY_LEVEL_TURNS
    elif level == "h":
        return HARD_LEVEL_TURNS



game_over = False

def check(random, user):
    if(random == user):
        print("You won")
        game_over = True
    elif(random > user):
        print("Your guess is too low")
    elif(random < user):
        print("Your guess is too high")

def check_gameover(turn):
    if(turn == 0):
        print("Game Over")
        global game_over 
        game_over = True
    
def game():
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    random_number = random.randint(1,101)
    turn = set_difficulty()


    while(not game_over):
        User_input = int(input("Input a number between 1, 100\n"))
        check(random_number, User_input)
        turn = turn - 1
        print(f"You have {turn} lives left ")
        check_gameover(turn)


game()

