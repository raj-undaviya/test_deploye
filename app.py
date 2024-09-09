from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello, World! This is my Flask app running on Python 3.12."

if __name__ == '__main__':
    app.run(debug=True)