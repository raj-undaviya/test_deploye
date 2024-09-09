from flask import Flask, render_template

app = Flask(__name__)

app.secret_key = "your_secret_key"
app.config['SESSION_COOKIE_EXPIRES'] = None

@app.route('/')
def hello():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)