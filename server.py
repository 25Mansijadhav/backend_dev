from flask import Flask

app = Flask(__name__)

@app.route('/', methods=['GET'])
def root():
    return "flask app"

app.run(host="0.0.0.0", port=6200)