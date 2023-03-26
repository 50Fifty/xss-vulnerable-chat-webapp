from flask import Flask, request

app = Flask(__name__)

@app.route("/listen", methods=['POST'])
def listen():
    if request.method == 'POST':
        print(request.form['cookie'])
        return "OK"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5001)
