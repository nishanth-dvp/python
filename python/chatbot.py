from os import name

def chatbot(message):

    if message == "hello":
        return "Hi!"
   
    if message== "hi":
        return "Hello!"
    
    if message == "how are you":
        return "I'm fine, thanks!"

    if message == "bye":
        return "Goodbye!"
    
    if message == "what is your name":
        return "I am a chatbot."

    else:
        return "Sorry, I don't understand."


print("===== Basic Chatbot =====")
print("Type 'bye' to exit.")
name=input("Enter your name: ")
while True:
    user = input(f"{name}: ").lower()

    reply = chatbot(user)

    print("meya:", reply)

    if user == "bye":
        break