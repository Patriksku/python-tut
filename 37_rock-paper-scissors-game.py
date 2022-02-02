import random


while True:
    choices = ["rock", "paper", "scissors"]
    player = None
    computer = random.choice(choices)

    while player not in choices:
        player = input("rock, paper or scissors?: ").lower()

    print("Player:", player)
    print("Computer:", computer)

    if player == computer:
        print("Tie!")

    elif player == "rock":
        if computer == "paper":
            print("You lose!")
        if computer == "scissors":
            print("You win!")

    elif player == "scissors":
        if computer == "rock":
            print("You lose!")
        if computer == "paper":
            print("You win!")

    elif player == "paper":
        if computer == "scissors":
            print("You lose!")
        if computer == "rock":
            print("You win!")

    play_again = input("Play again? (y/n): ").lower()
    print(play_again)

    if play_again != "yes" and play_again != "y":
        break

print("Good game!")


