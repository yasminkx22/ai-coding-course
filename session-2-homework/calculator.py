from datetime import datetime

def run_calculator():
    print("--- 🔢 Calculator with Memory ---")
    
    # 1. Get user input
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
    except ValueError:
        print("❌ Error: Please enter valid numbers.")
        return

    # 2. Perform Calculations
    add = num1 + num2
    sub = num1 - num2
    mult = num1 * num2
    
    # Handle Division by Zero
    if num2 != 0:
        div = round(num1 / num2, 2)
    else:
        div = "Undefined (Cannot divide by zero)"

    # 3. Create the timestamp
    timestamp = datetime.now().strftime("%b %d, %Y - %I:%M %p")

    # 4. Display Results to Console
    print(f"\nResults for {num1} and {num2}:")
    print(f"{num1} + {num2} = {add:.2f}")
    print(f"{num1} - {num2} = {sub:.2f}")
    print(f"{num1} × {num2} = {mult:.2f}")
    print(f"{num1} ÷ {num2} = {div:.2f}\n")

    # 5. Append to History File
    with open("calculator_history.txt", "a", encoding="utf-8") as file:
        file.write(f"[{timestamp}]\n")
        file.write(f"{num1} + {num2} = {add:.2f}\n")
        file.write(f"{num1} - {num2} = {sub:.2f}\n")
        file.write(f"{num1} × {num2} = {mult:.2f}\n")
        file.write(f"{num1} ÷ {num2} = {div:.2f}\n")
        file.write("-" * 30 + "\n") # Separator for readability

    print("✅ Calculations saved to calculator_history.txt")

if __name__ == "__main__":
    run_calculator()