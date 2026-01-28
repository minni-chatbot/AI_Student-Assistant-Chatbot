print("Hello! I am Student Assistant Chatbot.")
print("Type 'exit' to stop.\n")

while True:
    user_input = input("You: ").lower()

    if user_input == "exit":
        print("Chatbot: Goodbye! Have a nice day 😊")
        break

    elif "ai" in user_input:
        print("Chatbot: AI stands for Artificial Intelligence.")

    elif "bca" in user_input:
        print("Chatbot: BCA stands for Bachelor of Computer Applications.")

    elif "python" in user_input:
        print("Chatbot: Python is a popular programming language.")

    elif "chatbot" in user_input:
        print("Chatbot: A chatbot is a program that talks with users.")

    else:
        print("Chatbot: Sorry, I don't understand that.")
    elif "subjects" in user_input:
        print("Chatbot: BCA subjects include Programming, DBMS, AI, Networking, and Web Technologies.")

    elif "exam" in user_input:
        print("Chatbot: Exams are usually conducted at the end of each semester.")

    elif "college" in user_input:
        print("Chatbot: This chatbot is designed to help college students.")

    elif "career" in user_input:
        print("Chatbot: After BCA, students can go for MCA, MBA, or IT jobs.")

    elif "help" in user_input:
        print("Chatbot: I can help you with BCA, AI, Python, and general queries.")
        