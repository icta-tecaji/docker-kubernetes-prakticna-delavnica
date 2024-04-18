import os
import time

import requests
from flask import Flask

app = Flask(__name__)
api_host_and_port = os.getenv("RND_API_HOST_AND_PORT", "localhost:5000")

def get_rnd_number():
    try:
        number = requests.get(f"http://{api_host_and_port}/rng")
        if number.status_code == 200:
            return int(number.json().get("number"))    
        else:
            return "Status error!"
    except BaseException as err:
        print(err, flush=True)
        return "Service unavailable!"

@app.route('/')
def hello():
    number = get_rnd_number()

    if isinstance(number, int):
        text = f"Random število je {number}"
    else:
        text = number
    return f"Pozdravljeni!\n {text}"

@app.route('/health')
def health():
    return "Status OK."

if __name__ == "__main__":
    app.run(host="0.0.0.0", port= 5000, debug=True)
