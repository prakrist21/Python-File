import random

# Predefined lists and dictionaries
agent_names = ["Alex", "Jamie", "Taylor", "Jordan", "John", "Jimmy", "Ryan", "Denis", "Roger"]
keywords_responses = {
    "name": ["The name of the college is The British College"],
    "hi": ["Hello, how can I help you?", "Welcome, how may I assist you?"],
    "principal": ["The name of our Principal is Dr. Patrick M."],
    "admission": [
        "The admission will start from the second week of September. For more details, contact us or visit our website www.www.com"
    ],
    "location": ["Our college is located in Thapathali, Kathmandu, Nepal"],
    "facilities": ["We have different facilities like sports, cafe, library, VR room, etc."],
}
generic_responses = [
    "Sorry, I am not trained for this.",
    "I don't have an answer for this.",
    "That's an interesting question! Let me get back to you on that.",
    "Hmm, I am not sure about that. Can you try rephrasing it?",
]
exit_keywords = ["quit", "exit", "bye"]

# Greeting and agent name setup
def get_agent_name():
    return random.choice(agent_names)

# Main chatbot function
def chatbot():
    user_name = input("Welcome! What's your name? ").strip()
    if not user_name:
        user_name = "Friend"  # Default name if user doesn't input one
    agent_name = get_agent_name()
    print(f"Hi {user_name}, I'm {agent_name}, your assistant!")
    print(f"Feel free to ask me anything about our college or type 'bye' to exit.")
    
    while True:
        user_input = input(f"{user_name}: ").strip().lower()
        if user_input in exit_keywords:
            confirmation = input("Are you sure you want to exit? (yes/no): ").strip().lower()
            if confirmation in ["yes", "y"]:
                print(f"{agent_name}: Goodbye, {user_name}! Take care!")
                break
            else:
                print(f"{agent_name}: Okay, let's continue!")
                continue
        
        # Keyword matching
        found_response = False
        input_words = set(user_input.split())
        for keyword in keywords_responses.keys():
            if keyword in input_words:
                print(f"{agent_name}: {random.choice(keywords_responses[keyword])}")
                found_response = True
                break
        
        # If no keyword matched, provide a random generic response
        if not found_response:
            print(f"{agent_name}: {random.choice(generic_responses)}")
        
        # Random disconnection simulation
        if random.random() < 0.1:  # 10% chance of disconnection
            print(f"{agent_name}: Oops, I seem to have disconnected. One moment...")
            print(f"{agent_name}: I'm back, {user_name}! Let's continue.")

chatbot()