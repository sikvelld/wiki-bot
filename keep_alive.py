from flask import flask
from threading import Thread

app = flask('app')
@app.route('/')
def main():
    return "Бот"


def run():
    app.run(host="0.0.0.0", port = 8080)

def keep_alive():
    server = Thread(target=run)
    server.start()
