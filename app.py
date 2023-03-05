from flask import Flask, render_template, url_for, redirect, request
import json
app = Flask(__name__)

@app.route("/", methods = ('GET','POST'))
def receive():
    if request.method == 'POST':
        data = request.form['jsonData']
        with open('data.json','w') as f1:
            f1.write(data)
        return render_template('result.html', data = data)
    return render_template('index.html')
