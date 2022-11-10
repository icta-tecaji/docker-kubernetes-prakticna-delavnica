import random

from flask import Flask, Response, jsonify

app = Flask(__name__)
BREAK_APP_COUNTER = 5
error_count = 0

@app.route('/health')
def healthcheck():
    if error_count < BREAK_APP_COUNTER:
        return jsonify(status="up")
    else:
        return Response(f"Error", status=500)

@app.route('/rng')
def rng():
    global error_count
    print(f"Generating random number. Counter: {error_count}", flush=True)
    if error_count < BREAK_APP_COUNTER:
        rnd_number = random.randint(0,20)
        error_count += 1
        print(f"Random number: {rnd_number}", flush=True)
        return jsonify(number=rnd_number)
    else:
        raise ValueError("Error getting value")

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=False)
