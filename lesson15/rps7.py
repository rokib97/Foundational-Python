import sys
import random
from enum import Enum


def rps(name="player_one"):
    game_count = 0
    player_wins = 0
    python_wins = 0

    def play_rps():

        nonlocal player_wins
        nonlocal python_wins
        nonlocal name

        class RPS(Enum):
            ROCK = 1
            PAPER = 2
            SCISSORS = 3

        player_choise = input(
            f"\n{name}, enter...\n1 for Rock\n2 for Paper\n3 for Scissors:\n\n")

        if player_choise not in ["1", "2", "3"]:
            print(f"{name}, you must enter 1, 2 or 3.\nExiting The Game..")
            return play_rps()

        player = int(player_choise)
        computer_choose = random.randint(1, 3)
        computer = int(computer_choose)

        print(f"\n{name}, you choose {str(RPS(player)).replace('RPS.','')}.")
        print(f"Python choose {str(RPS(computer)).replace('RPS.','')}\n")

        def decide_winner(player, computer):
            nonlocal player_wins
            nonlocal python_wins
            nonlocal name
            if (player == 1 and computer == 3):
                player_wins += 1
                return f"🎉{name}, You win!"
            elif (player == 2 and computer == 1):
                player_wins += 1
                return f"🎉{name}, You win!"
            elif (player == 3 and computer == 2):
                player_wins += 1
                return f"🎉{name}, You win!"
            elif (player == computer):
                return "😨 Tie Game!"
            else:
                python_wins += 1
                return f"🐍Python wins!\nSorry, {name}....😢"
        game_result = decide_winner(player, computer)
        print(game_result)

        nonlocal game_count
        game_count += 1

        print(f'\nGame Count: {game_count}')
        print(f'\n{name}\'s Wins: {player_wins}')
        print(f'\nPython Wins: {python_wins}')
        print(f"\nPlay Again?, {name}")

        while True:
            play_again = input("\nY for YES! or \nQ for QUIT\n")
            if play_again.lower() not in ["y", "q"]:
                continue
            else:
                break
        if (play_again .lower() == "y"):
            return play_rps()
        else:
            print("\n🎉🎉🎉🎉")
            print("Thank You For Playing!\n")
            sys.exit(f"Bye {name}! 👋")
    return play_rps


if __name__ == "__main__":

    import argparse

    parser = argparse.ArgumentParser(
        description="Provide a personl Game Experience!"
    )

    parser.add_argument(
        "-n", "--name", metavar="name",
        required=True, help="The name of the person playing the game!"
    )

    args = parser.parse_args()

    rock_paper_scissors = rps(args.name)
    rock_paper_scissors()
