from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)


@app.route('/')
def redir():
    return redirect(url_for("home"))


@app.route('/home')
def home():
    return render_template("index.html")


@app.route('/aboutme')
def aboutme():
    return render_template("aboutme.html")


@app.route('/allwork')
def allwork():
    return render_template("allwork.html")


if __name__ == "__main__":
    app.run(debug=True)
