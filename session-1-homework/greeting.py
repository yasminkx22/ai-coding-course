import time

def main():
    # SETUP: Colors and Styles
    BOLD = "\033[1m"
    CYAN = "\033[96m"
    YELLOW = "\033[93m"
    GREEN = "\033[92m"
    MAGENTA = "\033[95m"
    BLUE = "\033[94m"
    ORANGE = "\033[33m"
    RESET = "\033[0m"

    # ACT 1: The Casual Greeting
    print(f"{CYAN}Hello! 🌎{RESET}")
    print(f"{YELLOW}How is your day? ☀️{RESET}")
    day_status = input(">> ").lower().strip()

    print(f"{GREEN}How did the weekend go? 🥂{RESET}")
    weekend_status = input(">> ").lower().strip()

    print(f"{MAGENTA}What is your favorite hobby lately? 🎨{RESET}")
    hobby = input(">> ").lower().strip()

    print("\n---")
    print(f"I'm glad to hear your day is '{day_status},' and that your weekend was '{weekend_status}.'")
    print(f"Since you enjoy {hobby}, maybe you should find some time for that today!")
    print("---\n")
    
    # Bridge between the two parts
    time.sleep(2)
    print(f"{BOLD}Now ... let's get a bit more creative.{RESET}")
    time.sleep(1.5)

    # ACT 2: The Imaginative Questions
    
    # Question 1: Teleportation
    print(f"{BLUE}If you could teleport anywhere for lunch right now, where would it be? 🍕{RESET}")
    raw_location = input(">> ")
    location = raw_location
    
    print(f"{BOLD}...Scanning maps for {location}...{RESET}")
    time.sleep(1.5) 

    # Question 2: Color Personality
    print(f"\n{ORANGE}If you were a color, which one would you be and why? 🎨{RESET}")
    raw_color = input(">> ")
    color_vibe = raw_color
    
    time.sleep(0.8)
    print("Interesting choice. I'm visualizing that energy now...")
    time.sleep(2) 

    # Question 3: Superpower
    print(f"\n{CYAN}What is a 'useless' superpower you'd actually love to have? 🦸{RESET}")
    superpower = input(">> ")
    
    # THE FINALE: Connecting the Dots
    print(f"\n{GREEN}[CONNECTING THE DOTS]{RESET}")
    time.sleep(2.5) 

    print("\n" + " ✨ " * 5)
    print(f"I've crunched the numbers.")
    time.sleep(1)
    print(f"Traveling to {BOLD}{location.capitalize()}{RESET} while feeling {BOLD}{color_vibe}{RESET} sounds like a vibe.")
    print(f"And honestly? Using your power to {BOLD}{superpower}{RESET} while you're there...")
    time.sleep(1)
    print("That is peak main-character energy. 🏆")
    print(" ✨ " * 5 + "\n")

if __name__ == "__main__":
    main()