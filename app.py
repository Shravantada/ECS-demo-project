from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, World! This is a Flask app."

if __name__ == '__main__':
<<<<<<< HEAD
<<<<<<< HEAD
    app.run(host='0.0.0.0', port=3000)
