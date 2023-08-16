import sys
import random
from enum import Enum


def rps(name="PlayerOne"):
    player_wins = 0
    python_wins = 0
    game_count = 0

    def play_rps():
        nonlocal player_wins
        nonlocal python_wins
        nonlocal name

        class RPS(Enum):
            ROCK = 1
            PAPPER = 2
            SCISSORS = 3
        try:
            player_choice = input(
                f"\n{name}, please enter...\n1 for rock,\n2 for paper,\n3 for scissor,\n\n")
            player = int(player_choice)
        except ValueError:
            print("Invalid input. Only integers can be entered.")

        if player_choice not in ["1", "2", "3"]:
            print(f"{name},please need to Enter 1,2 or 3...")
            return play_rps()

        computer_choice = random.choice("123")
        computer = int(computer_choice)

        print(f"\n{name}, choose {str(RPS(player)).replace('RPS.','')}.")
        print(f"Computer Choose {str(RPS(computer)).replace('RPS.','')}.\n")

        # rock paper scissors
        def decide_winner(player, computer):
            nonlocal player_wins
            nonlocal python_wins
            nonlocal name
            if player == 1 and computer == 3:
                player_wins += 1
                return f"🎉 {name}, you Win!"
            elif player == 2 and computer == 1:
                player_wins += 1
                return f"🎉 {name}, you Win!"
            elif player == 3 and computer == 2:
                player_wins += 1
                return f"🎉 {name}, you Win!"
            elif player == computer:
                return "😳 Tie Game!"
            else:
                python_wins += 1
                return f"🐍Python Wins!\nSorry {name}...😢😢😢"
        game_result = decide_winner(player, computer)
        print(game_result)

        nonlocal game_count
        game_count += 1
        print(f'\nGame Count: {game_count}')
        print(f'\n{name}\'s Wins: {player_wins}')
        print(f'\nPython Wins: {python_wins}')
        print(f"\nPlay again, {name}?")
        while True:
            play_again = input(" \nY for Yes or \nQ for Quit.\n")
            if play_again.lower() not in ["y", "q"]:
                continue
            else:
                break
        if play_again.lower() == 'y':
            return play_rps()
        else:
            print("\n🎉🎉🎉🎉🎉")
            print("Thank You For Playing....\n")
            sys.exit(f"Bye...{name} 👋")
    return play_rps


if __name__ == "__main__":

    import argparse

    parser = argparse.ArgumentParser(
        description="provide a personalized game experience!"
    )

    parser.add_argument(
        "-n", "--name", metavar="name", required=True,
        help="name of the player"
    )

    args = parser.parse_args()

    rock_paper_scissors = rps(args.name)
    rock_paper_scissors()
