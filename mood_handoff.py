from agents import Agent, Runner

# Agent 1: Mood Detector
mood_detector = Agent(
    name="Mood Detector",
    goal="Detect user's mood based on their message",
    handle=lambda message: detect_mood(message)
)

# Agent 2: Activity Suggester
activity_suggester = Agent(
    name="Activity Suggester",
    goal="Suggest a helpful activity for someone who is sad or stressed",
    handle=lambda mood: suggest_activity(mood)
)

# Simple logic for mood detection
def detect_mood(message):
    message = message.lower()
    if any(word in message for word in ['sad', 'unhappy', 'depressed']):
        return "sad"
    elif any(word in message for word in ['stressed', 'anxious', 'worried']):
        return "stressed"
    elif any(word in message for word in ['happy', 'joyful']):
        return "happy"
    else:
        return "neutral"

# Simple logic for activity suggestion
def suggest_activity(mood):
    if mood == "sad":
        return "Watch a comedy or call a friend."
    elif mood == "stressed":
        return "Take deep breaths or go for a walk."
    else:
        return "You're fine! Keep going!"

# Runner
if __name__ == "__main__":
    user_input = input("How are you feeling today? ")

    # Run Agent 1
    mood = Runner.run(mood_detector, user_input)
    print(f"\nDetected Mood: {mood}")

    # Conditional handoff to Agent 2
    if mood in ["sad", "stressed"]:
        suggestion = Runner.run(activity_suggester, mood)
        print(f"Suggested Activity: {suggestion}")
    else:
        print("No activity needed. Stay positive! 😊")
