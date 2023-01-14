from rockPaperScissor import *
from mathgame import *


# more games are coming soon......

while True:
    print("\n\nWelcome to 2-in-1 games")
    print("Choose the games from the list\n")
    print("Press(1) - ROCK, PAPER, SCISSOR\nPress(2) - MATH QUIZ\nPress(3) -QUIT")
    user_input = int(input())
    if user_input == 1:
        game1()
    elif user_input == 2:
        game2()
    elif user_input == 3:
        sys.exit()
    else:
        print("Invalid input")