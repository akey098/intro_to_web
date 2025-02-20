from flask import Flask

#1
app = Flask(__name__)
@app.route('/')
def index():
    return "<h1>Hello World!</h1>"

if __name__ == '__main__':
    app.run(debug=True)

#2
from flask import Flask
from markupsafe import escape

app = Flask(__name__)
@app.route('/')
def index():
    return "<h1>Hello World!</h1>"

@app.route('/greet/<name>')
def greet(name):
    return f"<h1>Hello, {escape(name.capitalize())}!</h1>"

if __name__ == '__main__':
    app.run(debug=True)

#3
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    names = ["Adilet", "Aziret", "Aidai"]
    return render_template('index.html', names=names, title="Welcome")

if __name__ == '__main__':
    app.run(debug=True)