from logging import debug
from pymongo import MongoClient
from flask import Flask, render_template, request, session, url_for, flash, redirect
import os
from dotenv import load_dotenv
from pathlib import Path

load_dotenv(dotenv_path=Path("./lmfao.env"))

mongoclient = os.getenv("mongoclient")
SECRET_KEY=os.getenv("SECRET_KEY")

client = MongoClient(mongoclient)
users= client.users

app = Flask(__name__)

app.config['SECRET_KEY'] = SECRET_KEY
  
@app.route('/', methods=('GET', 'POST'))
def templateFunc():
    if (request.method == 'POST'):
        user = request.form['user']
        session['username'] = user
        passVar = request.form['pass']
        session['password'] = passVar
        template = {
            'username': user,
            'password': passVar
        }
        findRes = users.users.find_one(template)
        if(findRes):
            session['admin'] = request.form['user']
            return redirect('next-page')
        else:
            flash("Incorrect Username-Password Combination")
    return render_template('index.html')

@app.route('/sign-up', methods=('GET', 'POST'))
def signUp():
    if (request.method == 'POST'):
        user = request.form['user']
        session['username'] = user
        passVar = request.form['pass']
        session['password'] = passVar
        template = {
            'username': user,
            'password': passVar
        }
        findRes = users.users.find_one(template)
        if not findRes:
            users.users.insert_one(template)
            return redirect('/')
        else:
            flash("This Username-Password Combination already exists!")
    return render_template('signup.html')

@app.route('/next-page', methods=('GET', 'POST'))
def nextPage():
    if 'username' not in session:
        return redirect('/')
    if (request.method == 'POST'):
        onVar = request.form['lmfao']
        if onVar == "on":
            print("on")
    return render_template('calender.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3333, debug=True)



