import random

while True:
    user_action = input("Choose your Fighter! (Naruto, Sasuke, Gaara): ")
    possible_actions = ["Naruto", "Sasuke", "Gaara"]
    computer_action = random.choice(possible_actions)
    print(f"\nYou chose {user_action}, computer chose {computer_action}.\n")

    if user_action == computer_action:
        print(f"Same Fighter! {user_action}. It's a tie!")
    elif user_action == "Naruto":
        if computer_action == "Gaara":
            print("Naruto uses Rasenshuriken to defeat Gaara! You win!")
        else:
            print("Susuke deflect Naruto's Rasenshuriken! You lose.")
    elif user_action == "Sasuke":
        if computer_action == "Naruto":
            print(" Sasuke uses Devine Departure to defeat Naruto! You win!")
        else:
            print("Gaara uses Sand Manipulation to choke Sasuke! You lose.")
    elif user_action == "Gaara":
        if computer_action == "Sasuke":
            print("Gaara uses Sand Manipulation to Blewed up's on Sasuke's face! You win!")
        else:
            print("Naruto uses Rasenshuriken to destroy Gaara! You lose.")

    play_again = input("Fight Again!? (y/n): ")
    if play_again.lower() != "y":
        break
        
