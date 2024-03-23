from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/flask_project'
db = SQLAlchemy(app)

class User(db.Model):
        __tablename__ = 'users'
        name = db.Column(db.String(255), nullable=False)
        lastname = db.Column(db.String(255), nullable=False)
        username = db.Column(db.String(255), unique=True, nullable=False,  primary_key=True)
        password = db.Column(db.String(255), nullable=False)
        
class Front_engine(db.Model):
        __tablename__ = 'front_engine'
        rpm = db.Column(db.Double(), unique=True, nullable=False, primary_key=True)
        o2 = db.Column(db.Double(), nullable=False)
        o2_v = db.Column(db.Double(), nullable=False)
        inj = db.Column(db.Double(), nullable=False)
        adv = db.Column(db.Double(), nullable=False)
        tps_v = db.Column(db.Double(), nullable=False)
        map = db.Column(db.Double(), nullable=False)
        map_v = db.Column(db.Double(), nullable=False)
        ve = db.Column(db.Double(), nullable=False)

class Rear_engine(db.Model):
        __tablename__ = 'rear_engine'
        rpm = db.Column(db.Double(), unique=True, nullable=False, primary_key=True)
        o2 = db.Column(db.Double(), nullable=False)
        o2_v = db.Column(db.Double(), nullable=False)
        inj = db.Column(db.Double(), nullable=False)
        adv = db.Column(db.Double(), nullable=False)
        tps_v = db.Column(db.Double(), nullable=False)
        map = db.Column(db.Double(), nullable=False)
        map_v = db.Column(db.Double(), nullable=False)
        ve = db.Column(db.Double(), nullable=False)


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
