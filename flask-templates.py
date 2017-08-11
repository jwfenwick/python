from flask import Flask
from flask import render_template
from random import randint

app = Flask(__name__)

@app.route('/')
def lucky():
    randomnum = randint(1,99)
    return render_template("lucky.html",lucky_num=randomnum)

if __name__ == "__main__":
    app.run()

