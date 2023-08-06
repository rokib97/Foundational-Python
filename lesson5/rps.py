import sys
import random
from enum import Enum
# value = input("Please input something...\n")
# print(value)

class RPS(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3
# print(RPS.ROCK.name)
# print(RPS(2))
# print(RPS.ROCK)
# print(RPS["ROCK"])
# print(RPS.SCISSORS.value)
# sys.exit()

print("")
player_choise = input("Enter...\n1 for Rock\n2 for Paper\n3 for Scissors:\n\n")
player = int(player_choise)

if(player < 1 or player > 3):
    sys.exit("You must enter 1, 2 or 3.\nExiting The Game..")
    
computer_choose = random.randint(1,3)
computer = int(computer_choose)
print("")
print("You choose " + str(RPS(player)).replace("RPS.","") + ".")
print("Python choose " + str(RPS(computer)).replace("RPS.","") + ".")
print("")

# 1 ==> Rock  
# 2 ==> Paper  
# 3 ==> Scissors

# Rock crushes scissors.
# Scissors cut paper.
# Paper covers rock.

# rock > scissors
# scissors > paper 
# paper > rock 

# rock > scissors > paper > rock 

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