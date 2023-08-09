import sys
import random
from enum import Enum

game_count = 0
def play_rps():
    class RPS(Enum):
        ROCK = 1
        PAPER = 2
        SCISSORS = 3
        
    player_choise = input("\nEnter...\n1 for Rock\n2 for Paper\n3 for Scissors:\n\n")
    
    if player_choise not in ["1","2","3"]:
        print("You must enter 1, 2 or 3.\nExiting The Game..")
        return play_rps()
    
    player = int(player_choise)
    computer_choose = random.randint(1,3)
    computer = int(computer_choose)

    print("\nYou choose " + str(RPS(player)).replace("RPS.","") + ".")
    print("Python choose " + str(RPS(computer)).replace("RPS.","") + ".\n")
    
    def decide_winner(player, computer):
        if(player == 1 and computer == 3):
            return"🎉 You win!"
        elif(player == 2 and computer == 1):
            return"🎉 You win!"
        elif(player == 3 and computer == 2):
            return"🎉 You win!"
        elif(player == computer):
            return"😨 Tie Game!"
        else:
            return"🐍Python wins!"
    game_result = decide_winner(player,computer)
    print(game_result)
    global game_count
    game_count += 1
    print('\nGame Count: ' + str(game_count))
    print("\nPlay Again?")
    while True:
        play_again  = input("\nY for YES! or \nQ for QUIT\n")
        if play_again.lower() not in ["y","q"]:
            continue
        else:
            break
    if(play_again .lower() == "y"):
        return play_rps()
    else:
        print("\n🎉🎉🎉🎉")
        print("Thank You For Playing!\n")
        sys.exit("Bye! 👋")

play_rps()