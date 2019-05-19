from flask import Flask, request, render_template
import pyrebase
from flask_sqlalchemy import SQLAlchemy
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
db = SQLAlchemy(app)
auth = firebase.auth()
db = firebase.database()
@app.route('/',  methods=["GET","POST"])
def index():
    try:
        if request.method == "POST":
            username = request.form['email']
            password = request.form['password']
            user = auth.sign_in_with_email_and_password(username,password)
            auth.get_account_info(user['idToken'])

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
            return render_template("index.html")
        except:
            return "registration failed"

    else:
        return render_template('register.html',value="Registration failed, try again.")

@app.route('/create')
def create():
    return render_template('create.html')

@app.route('/vote')
def vote():
    return render_template('vote.html')

@app.route('/path')
def vote():
    return render_template('vote.html')
if __name__ == '__main__':
    data = {
        ""
    }
    app.run(host="127.0.0.1", debug=True, port=5000)
