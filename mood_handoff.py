

def detect_mood(message):
    message = message.lower()
    if any(word in message for word in ["sad", "depressed", "unhappy"]):
        return "sad"
    elif any(word in message for word in ["stressed", "anxious", "worried"]):
        return "stressed"
    elif any(word in message for word in ["happy", "joyful", "excited"]):
        return "happy"
    elif any(word in message for word in ["angry", "mad"]):
        return "angry"
    else:
        return "neutral"

def suggest_activity(mood):
    if mood == "sad":
        return "Try watching a feel-good movie or calling a friend."
    elif mood == "stressed":
        return "Take a deep breath, walk a little, or listen to calm music."
    else:
        return None

def run_mood_check():
    user_input = input("How are you feeling today? ")
    mood = detect_mood(user_input)
    print(f"\nDetected Mood: {mood}")

    if mood in ["sad", "stressed"]:
        activity = suggest_activity(mood)
        print(f"Suggested Activity: {activity}")
    else:
        print("You're doing great! Keep going. 😊")


if __name__ == "__main__":
    run_mood_check()
