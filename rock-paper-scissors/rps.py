import sys
import random
from enum import Enum


class RPS(Enum):
    ROCK = 1
    PAPPER = 2
    SCISSORS = 3


play_again = True
while play_again:
    player_choice = input(
        "\nEnter...\n1 for rock,\n2 for paper,\n3 for scissor,\n\n")

    player = int(player_choice)

    if player < 1 or player > 3:
        sys.exit("You need to Enter 1,2 or 3...")

    computer_choice = random.choice("123")
    computer = int(computer_choice)

    print(f"\nYou choose {str(RPS(player)).replace('RPS.','')}.")
    print(f"Computer Choose {str(RPS(computer)).replace('RPS.','')}.\n")

    # rock paper scissors
    if player == 1 and computer == 3:
        print("🎉 You Win!")
    elif player == 2 and computer == 1:
        print("🎉 You Win!")
    elif player == 3 and computer == 2:
        print("🎉 You Win!")
    elif player == computer:
        print("😳 Tie Game!")
    else:
        print("🐍Python Wins!")

    play_again = input("\nPlay again? \nY for Yes or \nQ for Quit.\n\n")
    if play_again.lower() == 'y':
        continue
    else:
        print("\n🎉🎉🎉🎉🎉")
        print("Thank You For Playing....\n")
        play_again = False
        # break
sys.exit("Bye... 👋")
