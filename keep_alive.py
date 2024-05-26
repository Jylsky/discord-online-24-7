from flask import Flask
from threading import Thread
import os
app = Flask('')

@app.route('/')
def main():
    return '<meta http-equiv="refresh" content="0; URL=https://phantom.is-a.dev/support"/>'

def run():
    app.run(host="0.0.0.0", port=os.environ['port'])

def keep_alive():
    server = Thread(target=run)
    server.start()
