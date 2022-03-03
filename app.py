from logging import debug
from pymongo import MongoClient
from flask import Flask, render_template, request, session, url_for, flash, redirect
client = MongoClient("mongodb+srv://KabirIP:Kss2007@userpass.i0mli.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
users= client.users

app = Flask(__name__)

kabir = {
    'username': 'kabir',
    'password': 'Kss2007!'
}

app.config['SECRET_KEY'] = '28e1e2bcd63ffb5aaf6f613779122f41906c816b0dafad4f'
  
kabir = {
    'username': 'kabir',
    'password': 'Kss2007!'
}

brian = {
    'username': 'boyaredeez',
    'password': 'boyaredeez'
}
  
@app.route('/', methods=('GET', 'POST'))
def templateFunc():
    if (request.method == 'POST'):
        user = request.form['user']
        passVar = request.form['pass']
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
        passVar = request.form['pass']
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
    if 'admin' not in session:
        return redirect('/')
    if (request.method == 'POST'):
        onVar = request.form['lmfao']
    return render_template('calender.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3333, debug=True)



