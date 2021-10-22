import random

player_act = input("Enter a choice (rock, paper or scissors): ")
possible_acts = ["rock", "paper", "scissors"]
machine_act = random.choice(possible_acts)
print(f"\nYou chose {player_act}, computer chose {machine_act}.\n")

if player_act == machine_act:
    print(f"Both players selected {player_act}. It's a tie")
elif player_act == "rock":
    if machine_act == "scissors":
        print("You win")
    else:
        print("You lose.")
elif player_act == "paper":
    if machine_act == "rock":
        print("You win")
    else:
        print("You lose")
elif player_act == "scissors":
    if machine_act == "paper":
        print("You win")
    else:
        print("You lose")