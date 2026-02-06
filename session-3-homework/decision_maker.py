# Study Method Selector Program

def get_subject():
    """Asks the user what they are studying."""
    print("Welcome to the Study Method Selector!")
    return input("What subject are you studying today? (e.g., Math, History, Vocab): ").lower()

def get_time():
    """Asks how much time the user has in minutes."""
    while True:
        try:
            return int(input("How many minutes do you have to study? "))
        except ValueError:
            print("Please enter a number (e.g., 30 or 120).")

def get_learning_style():
    """Asks for the user's preferred learning style."""
    print("\nChoose your learning style:")
    print("A) Visual (Diagrams/Reading)")
    print("B) Auditory (Listening/Talking)")
    print("C) Kinesthetic (Doing/Practicing)")
    return input("Select A, B, or C: ").upper()

def determine_study_method(subject, time, style):
    """Logic engine that recommends a method based on user inputs."""
    
    # Logic Path 1: Short on time
    if time < 30:
        return "The Flashcard Sprint: Use Anki or Quizlet for rapid-fire recall."
    
    # Logic Path 2: Technical subjects with enough time
    elif subject in ["math", "science", "physics"] and time >= 60:
        return "The Feynman Technique: Try to explain a concept on a whiteboard as if to a child."
    
    # Logic Path 3: Humanities/Language with Visual style
    elif style == "A" and subject in ["history", "english", "vocab"]:
        return "Mind Mapping: Draw connections between themes and dates visually."
    
    # Logic Path 4: Large time blocks for any subject
    elif time >= 90:
        return "The Deep Work Session: 90 minutes of focused work with zero distractions."
    
    # Logic Path 5: General 'catch-all' for medium time
    else:
        return "The Pomodoro Technique: 25 minutes of focus followed by a 5-minute break."

def display_recommendation(method):
    """Outputs the final result to the user."""
    print("\n--- Your Recommendation ---")
    print(f"Based on your profile, you should use: {method}")
    print("Good luck with your session!")

# Main program - clean and simple
if __name__ == "__main__":
    # Gather information
    user_subject = get_subject()
    user_time = get_time()
    user_style = get_learning_style()
    
    # Process information
    recommendation = determine_study_method(user_subject, user_time, user_style)
    
    # Output results
    display_recommendation(recommendation)