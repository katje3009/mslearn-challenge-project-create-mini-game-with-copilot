# write rock, paper, scissors game
# if the player enters an invalid answer, the game asks the player to enter a valid answer
#add the end of each round the player is asked if they want to play again
# if yes, the game restarts
# if no, the game ends
# the game keeps track of the number of wins and losses of the player
# the game ends when the player decides to stop playing
# the game displays the number of wins and losses of the player at the end of the game
# inputs should be in lower case and player should be warned if the option is invalid

import random

def game():
    print("Welcome to Rock, Paper, Scissors!")
    wins = 0
    losses = 0
    while True:
        player = input("Enter rock, paper, or scissors: ")
        computer = random.choice(["rock", "paper", "scissors"])
        if player == computer:
            print(f"Both players selected {player}. It's a tie!")
        elif player == "rock":
            if computer == "scissors":
                print("Rock smashes scissors! You win!")
                wins += 1
            else:
                print("Paper covers rock! You lose.")
                losses += 1
        elif player == "paper":
            if computer == "rock":
                print("Paper covers rock! You win!")
                wins += 1
            else:
                print("Scissors cuts paper! You lose.")
                losses += 1
        elif player == "scissors":
            if computer == "paper":
                print("Scissors cuts paper! You win!")
                wins += 1
            else:
                print("Rock smashes scissors! You lose.")
                losses += 1
        else:
            print("Invalid input. Please enter rock, paper, or scissors.")
        print(f"Wins: {wins}, Losses: {losses}")
        play_again = input("Do you want to play again? (yes/no): ")
        if play_again.lower() != "yes":
            print("Thanks for playing!")
            break

game()


















