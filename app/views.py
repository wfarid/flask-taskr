
from flask import Flask, session, flash, redirect, url_for, request, render_template
from functools import wraps

app = Flask(__name__)

app.config.from_object('config')

def login_required(test):
    @wraps(test)
    def wrap(*args,**kwargs):
        if 'logged_in' in session:
            test(*args,**kwargs)
        else:
            flash('You need to login before accessing this page') #-- Why would we use flash() ?
            return redirect(url_for('login'))
    return wrap

'''
Q: Why do we need to support request methods POST and GET for the '/login' resource - if it can be called that
A: I think that we need to type the full url with the '/login' in the browser and so we need a to handle a GET
   request. When the user enter his credentials and press ENTER or the LOGIN/SUBMIT button, the request is POST
   that needs to be handled
'''
@app.route('/',methods=['GET','POST'])   
def login():
    if request.method == 'POST':
        if request.form['username'] != app.config['USERNAME'] or request.form['password'] != app.config['PASSWORD']:
            error = 'The username and/or password do not match our records'
            return render_template('login.html', error=error)
        else:
            session['logged_in'] = True
            return redirect(url_for('tasks'))

    return render_template('login.html')

@app.route('/logout')
@login_required
def logout():
    if 'logged_in' in session:
        session.pop('logged_in',None)
        flash('You were logged out')
        redirect(url_for('login'))

def get_db_connection():
    return sqlite.connect(app.config['DATABASE'])
