import sys
import random
from enum import Enum

class RPS(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3
    
is_playing = True  

while(is_playing):
    print(is_playing)
    player_choise = input("\nEnter...\n1 for Rock\n2 for Paper\n3 for Scissors:\n\n")
    player = int(player_choise)

    if(player < 1 or player > 3):
        sys.exit("You must enter 1, 2 or 3.\nExiting The Game..")
        
    computer_choose = random.randint(1,3)
    computer = int(computer_choose)

    print("\nYou choose " + str(RPS(player)).replace("RPS.","") + ".")
    print("Python choose " + str(RPS(computer)).replace("RPS.","") + ".\n")
    if(player == 1 and computer == 3):
        print("🎉 You win!")
    elif(player == 2 and computer == 1):
        print("🎉 You win!")
    elif(player == 3 and computer == 2):
        print("🎉 You win!")
    elif(player == computer):
        print("😨 Tie Game!")
    else:
        print("🐍Python wins!")

    play_again  = input("\nPlay Again? \nY for YES! or \nQ for QUIT\n\n")
    if(play_again .lower() == "y"):
        continue
    else:
        print("\n🎉🎉🎉🎉")
        print("Thank You For Playing!\n")
        is_playing = False

sys.exit("Bye! 👋")