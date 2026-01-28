# AI Student Assistant Chatbot
# Developed by Mini (BCA Student)
# Subject: Artificial Intelligence
# Description: This chatbot answers basic student-related questions
print("Hello! I am Student Assistant Chatbot.")
print("Type 'exit' to stop.\n")

while True:
    user_input = input("You: ").lower()
# Checking if user wants to know about exit
    if user_input == "exit":
        print("Chatbot: Goodbye! Have a nice day 😊")
        break
# Checking if user is asking about ai
    elif "ai" in user_input:
        print("Chatbot: AI stands for Artificial Intelligence.")

    elif "bca" in user_input:
        print("Chatbot: BCA stands for Bachelor of Computer Applications.")

    elif "python" in user_input:
        print("Chatbot: Python is a popular programming language.")
# Processing student quries
    elif "chatbot" in user_input:
        print("Chatbot: A chatbot is a program that talks with users.")
# If input doesn't match
    else:
        print("Chatbot: Sorry, I don't understand that.")
       
    elif "subjects" in user_input:
        print("Chatbot: BCA subjects include Programming, DBMS, AI, Networking, and Web Technologies.")
# Checking if user want to know about exam
    elif "exam" in user_input:
        print("Chatbot: Exams are usually conducted at the end of each semester.")

    elif "college" in user_input:
        print("Chatbot: This chatbot is designed to help college students.")

    elif "career" in user_input:
        print("Chatbot: After BCA, students can go for MCA, MBA, or IT jobs.")
# Provided chatbot response
    elif "help" in user_input:
        print("Chatbot: I can help you with BCA, AI, Python, and general queries.")
    

        
