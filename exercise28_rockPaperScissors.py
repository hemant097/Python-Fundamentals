import random

options = ("rock", "paper", "scissors")

running = True

while running:
    player = None
    computer = random.choice(options)

    #exists this inner loop, when one of the options is entered, else keeps repeating
    while player not in options:
        player = input("Enter your choice - rock, paper, or scissors ? ")

    print(f"Player chose {player}")
    print(f"Computer chose {computer}")

    if player == computer:
        print("Draw")
    elif player == "rock" and computer == "scissors":
        print("You win")
    elif player == "paper" and computer == "rock":
        print("You win")
    elif player == "scissors" and computer == "paper":
        print("You win")
    else:
        print("You lose, Computer wins")

    play_again = input("Want to play again, if yes press y else n? ").lower()
    if (not play_again == "y"):
        running = False

print("Thanks for playing")

