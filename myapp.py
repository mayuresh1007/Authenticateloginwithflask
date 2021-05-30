from flask import Flask,render_template,request,redirect,url_for,session 
from flask_sqlalchemy import SQLAlchemy 
from flask_login import LoginManager,UserMixin

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] ='sqlite:///presenty.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
login_manager= LoginManager()
login_manager.init_app(app)


class User(UserMixin, db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(25), unique=True, nullable=False)
    email = db.Column(db.String(25), unique=True, nullable=False)
    password = db.Column(db.String(20), unique=True, nullable=False)

    def __repr__(self) -> str:
        return f"{self.username} - {self.email} - {self.password}"

@login_manager.user_loader #()
def load_user(user_sno):
    return User.query.get(int(user_sno))

@app.route('/index', methods=['GET','POST'])
def index():
    if request.method=='POST': 
        # sno = request.form('sno')
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')
        user =User(username=username,email=email,password=password)
        db.session.add(user)
        db.session.commit()
        return redirect('/index')
    user = User.query.all() 
    return render_template('index.html',user=user)
    



if __name__ == "__main__":
    app.run(debug=True)