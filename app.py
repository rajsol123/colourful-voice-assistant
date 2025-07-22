from flask import Flask, render_template, jsonify
from assistant import take_command, handle_query
import threading

app = Flask(__name__)
response_log = []

def run_assistant():
    command = take_command()
    response = handle_query(command)
    response_log.append(f"User: {command}")
    response_log.append(f"Assistant: {response}")

@app.route('/')
def index():
    return render_template("index.html", logs=response_log)

@app.route('/listen', methods=['POST'])
def listen():
    thread = threading.Thread(target=run_assistant)
    thread.start()
    return jsonify({'status': 'Listening started'})

if __name__ == '__main__':
    app.run(debug=True)
