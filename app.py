import flask
import sqlite3
import os
from flask import Flask, make_response, render_template, request, redirect


app = Flask(__name__)

@app.route('/', methods = ['GET', 'POST'])
def index():
    if request.method =='POST':
        return redirect('index.html')
    return render_template("index.html")

if __name__ == '__main__':
    port = os.getenv('PORT')
    app.run(host='0.0.0.0', port=port)