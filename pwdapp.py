from flask import Flask, render_template
from random import randrange
import random
import string

app = Flask(__name__)


@app.route("/")
@app.route("/home")
def home():
    return render_template("index.html")


@app.route("/result", methods=['POST'])
def result():
    pwd = ""
    pwd += str(randrange(1010, 9890))
    i = 0
    while i < 9:
        pwd = pwd + random.choice(string.ascii_lowercase)
        i += 1
    pwd = pwd + random.choice(string.ascii_uppercase)
    return render_template("index.html", pwd=pwd)


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", ssl_context='adhoc')

