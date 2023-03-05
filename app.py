from flask import Flask, render_template, url_for, redirect, request
import json
app = Flask(__name__)

@app.route("/")
def receive():
    if request.method == 'POST':
        data = json.load(request.form['jsonData'])

    return "<p>Hello, World!</p>"

