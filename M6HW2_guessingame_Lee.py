#Gussing game
#10 Nov 2017
#CTI 110 M6HW2 random number guessing name
#Jeffrey Lee
#Write a program that does the following:
#Generate a random number in the range of 1 through 100
#Ask the user to guess what the secret number is
#If the user’s guess is higher than the secret number
#the program should tell the user Too high, try again
#If the user’s guess is lower than the secret number
#the program should tell the user Too low, try again
#If the user guesses the number correctly, the program should congratulate the user!
#The program should then ask the user Play again? (y for yes)(n for no)

import random

def main(play_game):
    print("play game")

def guess():
    g = int(input("Guess the number: "))
    return g

def hint(x):
    if x > ans:
        print("Lower")
    elif x < ans:
        print("Higher")
    else:
        print(victory(x))

def victory(x):
    if x == ans:
        print("Congratulations!  You got it!")



ans = random.randint(1,100)

while True:
    x = guess() 
    if x != ans: 
        hint(x)
    elif x == ans:
        victory(x)
        replay = input("Would you like to play again? y/n: ").strip().lower()
        if replay == "y":
             ans = random.randint(1,100)
             continue
        else:
            print("Okay then.  Bye-bye.")
            break

main()








         
                 
      
