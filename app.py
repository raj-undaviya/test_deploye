from flask import Flask

app = Flask(__name__)

app.secret_key = "your_secret_key"
app.config['SESSION_COOKIE_EXPIRES'] = None

@app.route('/')
def hello():
    return "Hello, World! This is my Flask app running on Python 3.12."

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)