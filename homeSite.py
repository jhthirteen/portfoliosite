from flask import Flask, render_template
app = Flask(__name__)


@app.route("/")
def home():
    return render_template('home.html')

@app.route("/about")
def about():
    return "about me page in progress"

@app.route("/projects")
def projects():
    return "projects page in progress"

@app.route("/connect")
def connect():
    return "connections page in progress"

if __name__ == '__main__':
    app.run(debug=True)