from flask import Flask, render_template, redirect


import json

app = Flask(__name__)


@app.route('/<title>')
@app.route('/index/<title>')
def index(title):
    return render_template('index.html', title=title)

if __name__ =="__main__":
    app.run(port=8080, host="127.0.0.1")