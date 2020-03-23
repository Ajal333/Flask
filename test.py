from flask import Flask, url_for, render_template, request
from markupsafe import escape

app = Flask(__name__)

@app.route('/home')
@app.route('/index')
@app.route('/') 
def welcome() :
    return render_template('index.html')

@app.route('/lfh') 
def lfh() :
    return ('Welcome to Learn from home.')

@app.route('/profile/<username>')
def profile(username) :
    return render_template('profile.html',name = username)

@app.route('/login',methods = ['GET','POST'])
def login() :
    if request.method == 'POST' :
        name = request.form['name']
        college = request.form['college']
        native = request.form['native']
        return render_template('profile.html',name = name, college= college,native=native)
    return render_template('login.html')

if __name__ == '__main__' :
    app.run(debug=True)
