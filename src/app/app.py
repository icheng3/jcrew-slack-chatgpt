from slack_bolt import App
from vectorstore import vectorstore
from Retrievers import vector_store as vs
from slackbot import (SlackBot, SLACK_BOT_TOKEN)

app = App(token=SLACK_BOT_TOKEN)

chatbot = SlackBot(app, vectorstore, False)
#chatbot = SlackBot(app, vs.vectorstore, False)

@app.message(".*")
def message_handler(message, say, logger):
    chatbot.handle_message(message, say)

@app.event('app_mention')
def mention_handler(payload, say):
    chatbot.handle_mention(payload, say)
