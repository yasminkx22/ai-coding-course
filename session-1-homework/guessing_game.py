import random

def main():
    # Colors
    GOLD = "\033[93m"
    RED = "\033[91m"
    BLUE = "\033[94m"
    CYAN = "\033[96m"
    BOLD = "\033[1m"
    RESET = "\033[0m"

    print(f"{BOLD}{GOLD}🎮 THE GUESSING GAME 🎮{RESET}")
    print("----------------------------")
    print(f"1. {CYAN}Standard Mode{RESET} (Unlimited tries + Heat hints)")
    print(f"2. {RED}Extreme Mode{RESET} (5 Hearts + High stakes)")
    
    mode = input("\nChoose your path (1 or 2): ")

    # MODE 1: STANDARD (1-50)
    if mode == "1":
        secret = random.randint(1, 50)
        attempts = 0
        print(f"\n{BLUE}I've hidden a number between 1 and 50.{RESET}")
        
        while True:
            guess = int(input(f"{BOLD}Your guess: {RESET}"))
            attempts += 1
            distance = abs(secret - guess)

            if guess == secret:
                print(f"✨ {GOLD}CORRECT!{RESET} It took you {attempts} attempts.")
                break
            
            # The Heat System
            if distance <= 3:
                print(f"{RED}🔥 BURNING HOT!!{RESET}")
            elif distance <= 8:
                print(f"{GOLD}☀️ Getting warmer...{RESET}")
            elif distance <= 15:
                print(f"{BLUE}❄️ A bit chilly (Cold).{RESET}")
            else:
                print(f"{BOLD}🧊 ABSOLUTELY FREEZING!{RESET}")

            # Directional Hint
            if guess < secret:
                print("Hint: Try a higher number ↑")
            else: 
                print("Hint: Try a lower number ↓")

    # MODE 2: EXTREME (1-100)
    elif mode == "2":
        secret = random.randint(1, 100)
        lives = 5
        print(f"\n{RED}{BOLD}EXTREME MODE ACTIVATED.{RESET}")
        print("I'm thinking of a number between 1 and 100.")

        while lives > 0:
            print(f"\nHP: {'❤️' * lives}")
            guess = int(input("Vital Guess: "))

            if guess == secret:
                print(f"🏆 {GOLD}{BOLD}UNBELIEVABLE! You survived with {lives} lives left!{RESET}")
                break
            else:
                lives -= 1
                if lives > 0:
                    print(f"WRONG. {'Higher ↑' if guess < secret else 'Lower ↓'}")
                else:
                    print(f"\n💀 {RED}GAME OVER.{RESET}")
                    print(f"The number was: {BOLD}{secret}{RESET}")
    
    else:
        print("Selection not recognized.")

if __name__ == "__main__":
    main()