import time

def get_repetitions():
    """Asks the user how many times the timer should repeat."""
    while True:
        try:
            count = int(input("How many rounds of the countdown would you like? "))
            return count
        except ValueError:
            print("Please enter a valid whole number.")

def run_countdown_repeater(rounds):
    """Executes the nested loop logic to repeat the countdown."""
    # Outer loop: Repeats the entire sequence
    for r in range(1, rounds + 1):
        print(f"\n--- Starting Round {r} ---")
        
        # Inner loop: The actual countdown
        # range(start, stop, step) -> counts from 10 down to 1
        for i in range(10, 0, -1):
            print(f"{i}...")
            time.sleep(1) # Pauses for 1 second to simulate a real clock
            
        print("BLAST OFF! 🚀")

def display_finish_message():
    """Simple sign-off after all rounds are done."""
    print("\nAll rounds completed. Great job!")

# Main program
if __name__ == "__main__":
    # 1. Get user input
    total_rounds = get_repetitions()
    
    # 2. Run the loops
    run_countdown_repeater(total_rounds)
    
    # 3. Final output
    display_finish_message()