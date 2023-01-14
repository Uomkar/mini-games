import random, sys, time

def game1():
    print("Welcome to ROCK, PAPER, SCISSOR \U0001F600" )
    win = 0
    loss = 0
    tie = 0
                                    #main game loop

    while True:
        print(f"Wins:{win}, Losses:{loss}, Ties:{tie}")
        while True:                                                                                                        #input loop
            print("Enter your move: (r)ock, (p)paper, (s)cissor or (q)uit \ntype one of the following: r , p , s or q")

            player = input()
            if player == "q":
                sys.exit("Thank you for playing \U0001F64F")
            if player == "r" or player == "p" or player == "s":
                break                                                                                             # break out of the input loop


        #Display what player chose
        if player == "r":
            print("ROCKS\U0001F5FF v/s....")
            time.sleep(1)
        elif player == "p":
            print("PAPER\U0001F4C3 v/s....")
            time.sleep(1)
        elif player == "s":
            print("SCISSOR\U00002702 v/s....")
            time.sleep(1)

                                        # Display what computer chose
        randomNum = random.randint(1,3)
        if randomNum == 1:
            print("\U0001F5FF:ROCKS")
            computer = "r"
        elif randomNum ==2:
            print("\U0001F4C3PAPER")
            computer = "p"
        elif randomNum == 3:
            print("\U00002702SCISSOR")
            computer = "s"

                                   # wins, losses and tie tracker
        if player == computer:
            print('It is a tie!')
            tie = tie + 1
        elif player == 'r' and computer == 's':
            print('You win!')
            win = win + 1
        elif player == 'p' and computer == 'r':
            print('You win!')
            win = win + 1
        elif player == 's' and computer == 'p':
            print('You win!')
            win = win + 1
        elif player == 'r' and computer == 'p':
            print('You lose!')
            loss = loss + 1
        elif player == 'p' and computer == 's':
            print('You lose!')
            loss = loss + 1
        elif player == 's' and computer == 'r':
            print('You lose!')
            loss = loss + 1