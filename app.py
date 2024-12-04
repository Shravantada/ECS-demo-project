from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, World! This is a Flask app."

if __name__ == '__main__':
<<<<<<< HEAD
    app.run(host='0.0.0.0', port=8000)
    
    
=======
    app.run(host='0.0.0.0', port=5000)  # Runs on all available interfaces
>>>>>>> 8a8f6190758dad789d69f3d2a006da1f542fb7c5
