from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import pyrebase
from flask import Flask, request, render_template, redirect, url_for
app = Flask(__name__)
app.config['SQLAlCHEMY_DATABASE_URI'] = 'sqlite://site.db'
firebaseConfig = {
    "apiKey": "AIzaSyCEJUbIKPdjh9817ydlSpQlwoTKGFlxwz0",
    "authDomain": "blockvote-e7945.firebaseapp.com",
    "databaseURL": "https://blockvote-e7945.firebaseio.com",
    "projectId": "blockvote-e7945",
    "storageBucket": "blockvote-e7945.appspot.com",
    "messagingSenderId": "70448506085",
    "appId": "1:70448506085:web:a8dac621838a33e4"
  }

firebase = pyrebase.initialize_app(firebaseConfig)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)
auth = firebase.auth()

class Poll(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(240), unique=True, nullable=False)
    poll_options = db.relationship('PollOption',backref='pollpost',lazy=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    def __repr__(self):
        return f"Poll('{self.title}', '{self.poll_options}')"


class PollOption(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(240), unique=False, nullable=False)
    post_id = db.Column(db.Integer, db.ForeignKey('poll.id'),nullable=False)
    def __repr__(self):
        return f"PollOption('{self.content}')"


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique= True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    polls = db.relationship('Poll',backref='author', lazy=True)

    def __repr__(self):
        return f"User ('{self.email}', '{self.polls}')"

db.create_all()
@app.route('/',  methods=["GET","POST"])
def index():
    try:
        if request.method == "POST":
            username = request.form['email']
            password = request.form['password']
            user = auth.sign_in_with_email_and_password(username,password)
            return render_template("path.html")

    except:
        print("login failed")
    return render_template('index.html')


@app.route('/register', methods=["GET","POST"])
def register():
    if request.method == "POST":
        username = request.form['email']
        password = request.form['password']
        try:
            auth.create_user_with_email_and_password(username,password)
            user = User(email=username,password=password)
            db.session.add(user)
            db.session.commit()
            return redirect(url_for("index"))

        except:
            print(username, password)
    else:
        return render_template('register.html',value="Registration failed, try again.")

@app.route('/create')
def create():
    return render_template('create.html')

@app.route('/vote')
def vote():
    return render_template('vote.html')

@app.route('/path')
def path():
    return render_template('vote.html')

if __name__ == "__main__":
    app.run(host="127.0.0.1", debug=True, port=5000)