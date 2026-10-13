from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

chatbot = ChatBot("Chatpot")

trainer = ListTrainer(chatbot)

#Treinamento 1
trainer.train([
    "Hi",
    "Welcome, friend 🤗",
])

#Treinamento 2
trainer.train([
    "Are you a plant?",
    "No, I'm the pot below the plant!",
])

exit_conditions = (':q', 'quit', 'exit')
while True:
    query = input('> ')
    if query in exit_conditions:
        break
    else:
        print(f"🪴 {chatbot.get_response(query)}")