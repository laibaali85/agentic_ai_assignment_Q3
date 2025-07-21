# 1️⃣ Smart Store Agent
# File name: product_suggester.py

# Create an agent that suggests a product based on user needs.
# Example: If the user says "I have a headache", it should suggest a medicine and explain why.

def product_suggestor(user_input):
    user_input= user_input.lower()
    suggestion={
        "headache":("Paracetamol", "It helps relieve headaches by reducing inflammation"
        " and blocking pain signals."),
        "cough":("Cough Syrup ","It soothes the throat and suppresses the cough reflex, helping you breathe easier."),
        "fever": ("Ibuprofen", "It reduces fever and provides relief from inflammation."),
        "sore throat": ("Lozenges", "They help relieve pain and irritation in the throat."),
        "cold": ("Antihistamines", "They reduce sneezing, runny nose, and congestion."),
        "stomach ache": ("Antacids", "They neutralize stomach acid and relieve pain."),
        "allergy": ("Cetirizine", "It is an antihistamine that reduces allergy symptoms."),
        "dry skin": ("Moisturizing Cream", "It hydrates and repairs dry or cracked skin."),
        "dandruff": ("Anti-Dandruff Shampoo", "It removes dandruff and soothes the scalp."),
        "infection": ("Antibiotic (e.g. Amoxicillin)", "Antibiotics treat bacterial infections by killing or inhibiting the growth of bacteria."),
        "bone pain": ("Calcium + Vitamin D Supplement", "These strengthen bones and may help reduce bone pain due to deficiency."),
        "back pain": ("Muscle Relaxant Cream", "It helps relieve muscle tension and provides comfort for lower or upper back pain."),

    }

    for symptom, (product, reason) in suggestion.items():
        if symptom in user_input:
            return f"Suggested Product: {product}\nReason: {reason}"

    return "Sorry, I couldn't find a product for your need. Please try describing it differently."

if __name__ == "__main__":
    user_problem = input("Tell me what you need help with: ")
    result = product_suggestor(user_problem)
    print(result)
