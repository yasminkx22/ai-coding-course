from datetime import datetime

def create_time_capsule():
    # 1. Dynamic Date Calculation
    now = datetime.now()
    today_date = now.strftime("%b %d, %Y")
    
    # Calculate exactly 10 years from today
    future_year = now.year + 10
    # .replace handles the year jump; strftime formats it beautifully
    future_date = now.replace(year=future_year).strftime("%b %d, %Y")
    
    filename = "time_capsule_2026.txt"
    
    print(f"--- 🕰️  TIME CAPSULE PROJECT (Today: {today_date}) ---")
    
    # 2. Questions
    questions = [
        ("Current Age", "How old are you?"),
        ("Favorite Song", "What is your current favorite song?"),
        ("Biggest Dream", "What is your biggest dream right now?"),
        ("Best Friend", "Who is your best friend?"),
        ("Current Mood", "How would you describe your life in one word?"),
        ("Future Goal", "Where do you want to be in 10 years?"),
        ("Message to Self", "Write a short note to your future self:")
    ]

    results = {}
    for label, prompt in questions:
        results[label] = input(f"{prompt} ")

    # 3. Save to file with box-drawing characters
    try:
        with open(filename, "w", encoding="utf-8") as f:
            # The header box
            f.write("╔════════════════════════════════════╗\n")
            f.write(f"║         TIME CAPSULE - {now.year}        ║\n")
            f.write(f"║        Created: {today_date:<19}║\n")
            f.write(f"║    To be opened in: {future_date:<13}  ║\n")
            f.write("╚════════════════════════════════════╝\n\n")

            f.write("--- YOUR LIFE SNAPSHOT ---\n")
            
            # Formatting the answers
            for label, answer in results.items():
                # f-string padding :<15 ensures the labels align
                f.write(f"{label + ':':<18} {answer}\n")

        print(f"\n✨ Sealed! Your capsule is saved as {filename}.")
        
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    create_time_capsule()