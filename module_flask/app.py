"""
# Flask login Example and instagram fallowing find
# https://niceman.tistory.com/191
"""
from flask import (
                Flask,
                url_for,
                render_template,
                request,
                redirect,
                session,
            )
from flask_sqlalchemy import SQLAlchemy
# from instagram import getfollowedby, getname

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)


class user(db.Model):
    """ Create User Table """
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    password = db.Column(db.String(80))

    def __init__(self, username, password):
        self.username = username
        self.password = password


@app.route('/', methods=['GET', 'POST'])
def home():
    """ Session control """
    if not session.get('logged_in'):
        return render_template('index.html')
    else:
        if request.method == 'POST':
            username = getname(request.form['username'])
            return render_template('index.html', data=getfollowedby(username))
        return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    """ login form """
    if request.method == 'GET':
        return render_template('index.html', data=getfollowedby(username))
    else:
        name = request.form['username']
        passw = request.form['password']

        try:
            data = user.query.filter_by(username=name, password=passw).first()
            if data is not None:
                session['logged_in'] = True
                return redirect(url_for('home'))
            else:
                return 'Dont Login'
        except:
            return 'Dont Login'


@app.route('/register', methods=['GET', 'POST'])
def register():
    """ register form """
    if request.method == 'POST':
        new_user = User(username=request.form['username'], password=request.form['password'])
        db.session.add(new_user)
        db.session.commit()
        return render_template('login.html')
    return render_template('register.html')


@app.route('/logout')
def logout():
    """ """
    session['logged_in'] = False
    return redirect(url_for('home'))



if __name__ == '__main__':
    app.debug = True
    db.create_all()
    app.secret_key = "123"
    app.run(host='0.0.0.0')
