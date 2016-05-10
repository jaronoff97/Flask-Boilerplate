import os
from datetime import datetime
from flask import Flask, request, flash, url_for, redirect, \
    render_template, abort, send_from_directory, jsonify
import json

app = Flask(__name__)
app.config.from_pyfile('flaskapp.cfg')


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/<path:resource>')
def serveStaticResource(resource):
    return send_from_directory('static/', resource)


@app.route("/test")
def test():
    print 'TEST @/test'
    return "<h1>This is a test</h1>\
    <h1>Fridge</h1>\
    <h1>Flask</h1>\
    <h1>Email</h1>\
    <h1>jacob_aronoff16@milton.edu</h1>"


@app.route("/getTest")
def gettest():
    return json.dumps({"status": "success"})


if __name__ == '__main__':
    app.run()
