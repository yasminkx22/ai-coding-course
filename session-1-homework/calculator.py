import math

def main():
    # Colors
    CYAN = "\033[96m"
    YELLOW = "\033[93m"
    GREEN = "\033[92m"
    MAGENTA = "\033[95m"
    BOLD = "\033[1m"
    RESET = "\033[0m"

    print(f"{BOLD}{MAGENTA}🚀 UNIVERSAL CALCULATOR 🚀{RESET}")
    print("-----------------------------")
    
    # The Menu
    print(f"{YELLOW}Select an operation category:{RESET}")
    print("1. Basic Math (+, -, *, /)")
    print("2. Power moves (Exponents & Roots)")
    print("3. Geometry (Area of a Circle)")
    print("4. Factorials")
    
    choice = input(f"\n{BOLD}Enter choice (1-4): {RESET}")

    # CATEGORY 1: BASIC MATH
    if choice == "1":
        num1 = float(input("First number: "))
        op = input("Operation (+, -, *, /): ")
        num2 = float(input("Second number: "))
        
        if op == "+": result = num1 + num2
        elif op == "-": result = num1 - num2
        elif op == "*": result = num1 * num2
        elif op == "/": result = num1 / num2 if num2 != 0 else "Error (Div by 0)"
        print(f"\n{GREEN}Result: {result}{RESET}")

    # CATEGORY 2: POWERS & ROOTS 
    elif choice == "2":
        num = float(input("Enter number: "))
        print("A) Square it (**2) | B) Cube it (**3) | C) Square Root")
        sub_choice = input(">> ").upper()
        
        if sub_choice == "A": result = num ** 2
        elif sub_choice == "B": result = num ** 3
        elif sub_choice == "C": result = math.sqrt(num)
        print(f"\n{GREEN}Result: {result}{RESET}")

    # CATEGORY 3: GEOMETRY
    elif choice == "3":
        radius = float(input("Enter the radius of the circle: "))
        # Area = Pi * r^2
        area = math.pi * (radius ** 2)
        print(f"\n{GREEN}The Area is: {round(area, 2)}{RESET}")

    # CATEGORY 4: FACTORIALS
    elif choice == "4":
        num = int(input("Enter a whole number: "))
        result = math.factorial(num)
        print(f"\n{GREEN}{num}! is: {result}{RESET}")

    else:
        print("That wasn't an option! Try again.")

    print("\n" + " ✨ " * 5)
    print(f"{BOLD}Calculation Complete.{RESET}")

if __name__ == "__main__":
    main()