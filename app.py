import random
import requests
from flask import Flask

URL = 'https://gist.githubusercontent.com/chuckwagoncomputing/ff980f81482b5894c824/raw/c54c87a325454a5ae91b6254fa4c30121e0891f5/excuses.txt'

app = Flask(__name__)

@app.route("/")
def bofh():

    dataset = requests.get(URL).text
    choice = random.choice(dataset.split('\n'))
    return choice

if __name__ == '__main__':
    # Finally start the app
    app.run(host='0.0.0.0', port=8080)
