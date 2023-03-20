from flask import Flask
from flask import render_template
from flask_socketio import SocketIO

app = Flask(__name__)
app.config["SECRET_KEY"] = 'secret!'
socketio = SocketIO(app)

messages = []


@app.route("/")
def hello():
    print(messages)
    return render_template('index.html', messages=messages)

@socketio.on('connect')
def test_connect():
    print('Client connected:')

@socketio.on('connected')
def connected_event(json):
    print('Received json: ' + str(json))

@socketio.on('send message')
def handle_message(json):
    print('Received message: ' + str(json))
    messages.append(json['data'])
    socketio.emit('receive message', json)


if __name__ == "__main__":
    socketio.run(app, "0.0.0.0")