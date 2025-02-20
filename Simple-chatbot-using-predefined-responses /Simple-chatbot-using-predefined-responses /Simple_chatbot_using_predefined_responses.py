#import the regular expression module to handle pattern matching
import re

#A dictionary that maps keywords to predefined responses 
responses = {
    "hello": "Hi there! How can I assist you today?",
    "help": "I'm here to help! What do you need assistance with?",
    "python": "Python is a versatile programming language. Do you need help with coding?",
    "error": "Could you provide the error message? I'll try to help you fix it.",
    "bye": "Goodbye! Have a great day!",
    "thank you": "You're welcome! Happy to help!",
    "ai": "Artificial Intelligence is a fascinating field! What aspect interests you?",
    "project": "Tell me more about your project. I’d love to help!",
    "vs code": "Are you facing any issues in VS Code? Let me know!",
    "tensorflow": "TensorFlow is great for deep learning! Do you need help with it?"
}

#function to find the appropriate response based on the user's input 
def chatbot_responses(user_input):
  #convert user input to lowercase to make matching case-sensitive
  user_input = user_input.lower()
  # Fix: Change 'keywork' to 'keyword' in the loop
  for keyword in responses:  
    if re.search(keyword,user_input):
      return responses[keyword]
  # Fix: Add a default response to handle unmatched input
  return "I'm sorry, I didn't understand your request."
#main function to run the chatbot
def chatbot():
  print("Chatbot:Hello! I'm Lucky I'm here to assist you. (Type 'bye' to exit)")
  while True:
    #get user input 
    user_input =input("You: ")
    #if user types 'bye' exit the loop 
    if user_input.lower() == 'bye':
      print("Chatbot: Goodbye! Have a great day!")
      break
    #Get chatbot's response based on user input
    response=chatbot_responses(user_input)
    #Print chatbot's response 
    print(f"Chatbot:{response}")

#run the chatbot
chatbot()
