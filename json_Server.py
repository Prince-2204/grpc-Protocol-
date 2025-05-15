from flask import Flask, request, jsonify
import time

app = Flask(__name__)

@app.route('/sayhi', methods=['POST'])
def say_hi():
    start = time.time()
    data = request.json
    user = data.get("user")
    req = data.get("request")
    response_text = f"Request coming from user {user} and request is {req}\n Response is hi mate how are you"
    end = time.time()
    exec_time = end - start
    return jsonify({
        "message": response_text,
        "execution_time": exec_time
    })

if __name__ == "__main__":
    app.run(port=5000)
