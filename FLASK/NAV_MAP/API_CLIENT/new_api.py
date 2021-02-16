from flask import Flask, redirect, url_for, request, jsonify
import socket
from flask_cors import CORS

ip   = "127.0.0.1";
PORT = 80

app = Flask(__name__)
CORS(app)

@app.route('/navigation/<coordinates>')
def navigation(coordinates):
    byte_message = coordinates.encode()
    opened_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    opened_socket.sendto(byte_message, (ip, PORT))
    opened_socket.close()
    return jsonify(hello='world')

if __name__ == '__main__':
    app.run(debug=True)