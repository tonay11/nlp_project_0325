import random

# Define transformation rules
RULES = {
    "i am": "Why do you think you are {0}?",
    "i feel": "What makes you feel {0}?",
    "my": "Tell me more about your {0}.",
    "because": "Is that the real reason?",
    "yes": "You seem quite certain.",
    "no": "Why not?",
    "you": "Let's not talk about me, let's talk about you."
}

# Memory queue for storing responses
memory_queue = []

def eliza_generator(user_sentence):
    words = user_sentence.lower().split()
    
    # Identify the highest ranked keyword
    for keyword in RULES:
        if keyword in user_sentence:
            response_template = RULES[keyword]
            transformed_response = response_template.format(user_sentence.replace(keyword, '').strip())
            
            # Store in memory if keyword is 'my'
            if keyword == "my":
                memory_queue.append(transformed_response)
            
            return transformed_response
    
    # If no keyword found, retrieve from memory or use a generic response
    if memory_queue:
        return memory_queue.pop(0)
    else:
        return random.choice(["Tell me more.", "How does that make you feel?", "Why do you say that?"])

# Test conversation
print(eliza_generator("I am sad"))
print(eliza_generator("My father is strict"))
print(eliza_generator("Because he never listens to me"))
