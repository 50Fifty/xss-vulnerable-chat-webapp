from flask import Flask, request, redirect, url_for
from flask import render_template
from flask_socketio import SocketIO
from flask_login import LoginManager
from flask_cors import CORS
from models import User
from secrets import token_hex

from flask_login import login_user, logout_user, login_required, current_user

app = Flask(__name__)
app.config["SECRET_KEY"] = 'secret!'
socketio = SocketIO(app)

login_manager = LoginManager()
login_manager.init_app(app)

CORS(app)

messages = []
# sessions = dict()

@app.route("/", methods=['GET'])
def index():
    return render_template('login.html')
    
@app.route("/login", methods=['POST'])
def login():
    if request.method == 'POST':
        # print("POST")
        username = request.form['username']
        password = request.form['password']
        user = User.get(username)
        if user is not None and user.password == password:
            login_user(user)
            token = token_hex(16)
            user.add_active_user(token)
            return {
                "status"    : "success",
                "message"   : "Login successful!",
                "token"     : token,
                "username"  : username,
                "redirect"  : "chat"
            }
            # return url_for('chat') # maybe can give a token here? (in json format?)
        else:
            return {
                "status"    : "error",
                "message"   : "Invalid username or password.",
                "redirect"  : "/"
            }
            # return render_template('login.html', error_msg="Invalid username or password.")

@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

@app.route("/chat")
def chat():
    return render_template('chat.html', messages=messages)

@app.route("/isloggedin", methods=["POST"])
def hastoken():
    if request.method == 'POST':
        cookie = request.form['cookie']
        parts = cookie.split("; ")

        # Loop through each part to find the token parameter
        token = None
        for part in parts:
            if part.startswith("token="):
                # Extract the value of the token parameter
                token = part[len("token="):]
                break

        user = User.get_by_token(token)
        
        if user is not None:
            return {
                "status"    : "success",
                "message"   : "User is logged in.",
                "username"  : user.username
            }
        else:
            return {
                "status"    : "error",
                "message"   : "User is not logged in."
            }

@socketio.on('connect')
def test_connect():
    print('Client connected.')

@socketio.on('connected')
def connected_event(json):
    print('Received json: ' + str(json))

@socketio.on('send message')
def handle_message(json):
    print('Received message: ' + str(json))
    messages.append(json['data'])
    socketio.emit('receive message', json)

@login_manager.user_loader
def load_user(user_id):
    return User.get(user_id)


if __name__ == "__main__":
    socketio.run(app, "0.0.0.0")