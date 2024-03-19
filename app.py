from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/flask_project'
db = SQLAlchemy(app)

class User(db.Model):
    name = db.Column(db.String(255), nullable=False)
    lastname = db.Column(db.String(255), nullable=False)
    username = db.Column(db.String(255), unique=True, nullable=False,  primary_key=True)
    password = db.Column(db.String(255), nullable=False)

    __tablename__ = 'users'


@app.route('/', methods=["POST", "GET"])
def login():
    error = ''
    if request.method == "POST":
        uname = request.form["username"]
        passw = request.form["password"]
        user = User.query.filter_by(username=uname, password=passw).first()
        if user:
            return render_template('home.html')
        else:
            error = "Invalid username or password"
        
    return render_template('index.html',error=error)

if __name__ == '__main__':
    app.run(debug=True)
