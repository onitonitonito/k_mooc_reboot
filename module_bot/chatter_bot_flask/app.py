"""
# BUILDING A CHATBOT IN PYTHON USING FLASK – TUTORIAL
# SEPTEMBER 22, 2019 - http://bit.ly/2mtKcuv
"""
# PROJECT AND LIBRARIES SETUP
# I will be using PyCharm to develop this simple chatbot.
# Create a Flask project using PyCharm. Following libraries are required:
#   - chatterbot
#   - chatterbot-corpus
#   - pytz
#   - sqlite3
# print(__doc__)


#imports
from flask import Flask, render_template, request
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

#create chatbot
app = Flask(__name__)
englishBot = ChatBot("Chatterbot", storage_adapter="chatterbot.storage.SQLStorageAdapter")

#train the chatter bot for english
trainer = ChatterBotCorpusTrainer(englishBot)
trainer.train("chatterbot.corpus.english")


#define app routes
@app.route("/")
def index():
    return render_template("index.html")


#function for the bot response
@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    return str(englishBot.get_response(userText))


if __name__ == "__main__":
    app.run()
