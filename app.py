from flask import Flask, render_template, url_for, redirect, request
import json
app = Flask(__name__)

@app.route("/", methods = ('GET', 'POST'))
def receive():
    data = request.form['jsonData']
    if request.method == 'POST':
        data = json.load(request.form['jsonData'])
        return render_template('result.html', data = data)
    return render_template('index.html')


