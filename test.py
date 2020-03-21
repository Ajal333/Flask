from flask import Flask, url_for, render_template
from markupsafe import escape

app = Flask(__name__)

@app.route('/') 
def welcome() :
    return render_template('index.html')

@app.route('/lfh') 
def lfh() :
    return ('Welcome to Learn from home.')

@app.route('/profile/<username>')
def profile(username) :
    return render_template('profile.html',username = username)


if __name__ == '__main__' :
    app.run()
