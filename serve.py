from flask import Flask, request
import subprocess
import socket

app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def process_json():
    if request.method == 'POST':
        p = subprocess.Popen(['python3', 'stress_cpu.py'])
        return "stress run"
    elif request.method == 'GET':
        return socket.gethostname()
    else:
        raise NotImplementedError


if __name__ == "__main__":
    app.run(host='0.0.0.0')
