import random

def get_target_number():
    """Generates a random secret number between 1 and 20."""
    return random.randint(1, 20)

def play_single_round(secret_number):
    """Contains the while loop for guessing until the user is correct."""
    guess = None
    attempts = 0
    
    print("\nI'm thinking of a number between 1 and 20.")
    
    # Inner While Loop: Keeps asking until the guess is correct
    while guess != secret_number:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1
            
            if guess < secret_number:
                print("Too low! Try again.")
            elif guess > secret_number:
                print("Too high! Try again.")
            else:
                print(f"Correct! It took you {attempts} attempts.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def ask_to_replay():
    """Asks the user if they want to play again to control the outer loop."""
    choice = input("\nDo you want to play another round? (yes/no): ").lower()
    return choice == "yes" or choice == "y"

# Main program
if __name__ == "__main__":
    print("--- The Ultimate Number Guesser ---")
    
    keep_playing = True
    
    # Outer While Loop: Controls the game repetition
    while keep_playing:
        target = get_target_number()
        play_single_round(target)
        
        # Update the condition for the outer loop
        keep_playing = ask_to_replay()
        
    print("\nThanks for playing! See you next time.")