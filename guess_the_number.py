import art 
import random 

again_game = True
while again_game == True:
    print(art.logo)
    print("Welcome to the game Guess The Number")
    
    what_level = input("Choose the level, put 'easy' or 'hard'\n").lower()
    
    generating = random.randint(0,50)
    #chances = int
    def guess_number (chances):
        #Generating the number
        global generating  
    
        #Attempts of guessing the number
        chances_remaining = chances 
        guessed = False
        while  guessed == False:
            attempt_number = int(input("Put the number that you thinks is\n"))
            if attempt_number != generating:
                chances_remaining -= 1
                if chances_remaining == 0:
                    print(f"The number of attemps remaining: 0")
                    print("Sorry you lose")
                    guessed = True
                elif attempt_number < generating:
                    print(f"The number of attemps remaining: {chances_remaining}") 
                    print("The number is higher")
                else:
                    print(f"The number of attemps remaining: {chances_remaining}") 
                    print("The number is lower")
            else: 
                print(f"You're right the number is {generating} You WON!!")
                restart = print(input("Do you want to play again? press 'y' or 'n'\n"))
                if restart == "n":
                    again_game == False
                else: 
                    guessed = True
    
    if what_level == "easy":
        print("You have 10 chances, guess the number")
        guess_number (10)
    elif what_level == "hard":
        print("You have 5 chances, guess the number")
        guess_number (5)
