from logging import debug
from pymongo import MongoClient
from flask import Flask, render_template, request, session, url_for, flash, redirect
import os
from dotenv import load_dotenv
from pathlib import Path
from bson.objectid import ObjectId

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
        passVar = request.form['pass']
        template = {
            'username': user,
            'password': passVar
        }
        findRes = users.users.find_one(template, {'_id': 1})
        if(findRes):
            session['username'] = request.form['user']
            session['password'] = passVar
            session['id'] = str(findRes)[18:-3]
            print(session['id'])
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
    if ('username' and 'password') not in session:
        return redirect('/')
    orderList = []
    if (request.method == 'POST'):
        lmfao = request.form['lmfao']
        imo = request.form['imo']
        if lmfao == "lmfao":
            orderList.append("lmfao")
            print("lmfao")
        if imo == "imo":
            orderList.append("imods")
            print("imo")
            print(session['id'])
        
        for i in orderList:
            users.users.update_one({"_id": ObjectId(session['id'])}, {"$push": {"orders": i}}, False, True)
        
        return redirect('checkout-page')

@app.route('/checkout-page')
def checkOut():
    print("")

    return render_template('calender.html')
    min()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3333, debug=True)



