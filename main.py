from flask import Flask, request
import requests
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters


TOKEN = '<token>'

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World!'


def get_url(method):
    return "https://api.telegram.org/bot{}/{}".format(TOKEN, method)


def respond_to_update(update):
    data = {}
    data["chat_id"] = update["message"]["chat"]["id"]
    data["text"] = "I can hear you!"
    r = requests.post(get_url("sendMessage"), data=data)
    print(r)


@app.route("/{}".format(TOKEN), methods=["POST"])
def process_update():
    if request.method == "POST":
        update = request.get_json()
        if "message" in update:
            respond_to_update(update)
        return "ok!", 200
