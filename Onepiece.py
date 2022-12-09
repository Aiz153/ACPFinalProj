import random

while True:
    user_action = input("Choose your Fighter! (WhiteBeard, Roger, Oden): ")
    possible_actions = ["WhiteBeard", "Roger", "Oden"]
    computer_action = random.choice(possible_actions)
    print(f"\nYou chose {user_action}, computer chose {computer_action}.\n")

    if user_action == computer_action:
        print(f"Same Fighter! {user_action}. It's a tie!")
    elif user_action == "WhiteBeard":
        if computer_action == "Oden":
            print("WhiteBeard uses earthquake to smash Oden! You win!")
        else:
            print("Roger deflect WhiteBeard's Erthquake! You lose.")
    elif user_action == "Roger":
        if computer_action == "WhiteBeard":
            print(" Roger uses Devine Departure to defeat WhiteBeard! You win!")
        else:
            print("Oden uses enma to cut Roger! You lose.")
    elif user_action == "Oden":
        if computer_action == "Roger":
            print("Oden uses enma to put a scar on Roger's face! You win!")
        else:
            print("WhiteBeard uses earquake to smash Oden! You lose.")

    play_again = input("Fight Again!? (y/n): ")
    if play_again.lower() != "y":
        break
