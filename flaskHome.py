from logging import debug
#from pymongo import MongoClient
from flask import Flask, render_template, request, url_for, flash, redirect
import subprocess
import os
#client = MongoClient(port = 27017)
#users= client.users

app = Flask(__name__)

app.config['SECRET_KEY'] = '28e1e2bcd63ffb5aaf6f613779122f41906c816b0dafad4f'

kabir = {
    'username': 'kabir',
    'password': 'Kss2007!'
}

@app.route('/', methods=('GET', 'POST'))
def templateFunc():
    if (request.method == 'POST'):
        pass = request.form['pass']
        user = request.form['user']
        template = {
            'username': user,
            'password': pass
        }
        print(template)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3333)
