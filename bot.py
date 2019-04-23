from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.comparisons import levenshtein_distance
chatbot = ChatBot('Ron Obvious')

# Create a new trainer for the chatbot
trainer = ChatterBotCorpusTrainer(
    chatbot,
    preprocessors=["mypreprocessors.remove_symbols"],
    statement_comparison_function=levenshtein_distance
)

# Train the chatbot based on the english corpus
trainer.train("chatterbot.corpus.german")

# Get a response to an input statement
response = str(chatbot.get_response("Der Kuchen ist eine Luge."))
print("Response: " + response)