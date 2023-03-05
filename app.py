from flask import Flask, render_template, url_for, redirect, request, send_from_directory
import json
import mat
from pathlib import Path

root = Path(__file__).parent
UPLOAD_FOLDER = root
app = Flask(__name__)

@app.route("/", methods = ('GET','POST'))
def receive():
    if request.method == 'POST':
        data = request.form['jsonData']
        with open('data.json','w') as f1:
            f1.write(data)
            mat.plotit()
        return render_template('result.html', filename = "graph.png")
    return render_template('index.html')

@app.route('/<filename>')
def send_file(filename):
    return send_from_directory(UPLOAD_FOLDER, filename)