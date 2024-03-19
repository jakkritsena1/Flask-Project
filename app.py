from flask import Flask, render_template,request
from flask_mysql import MySQL

mysql = MySQL()
app = Flask(__name__)
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = ''
app.config['MYSQL_DATABASE_DB'] = 'flask_project'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'

mysql.init_app(app)

@app.route('/', methods=['POST', 'GET'])
def login():
    if request.method=="POST":
        uname = request.form["User"]
        passw = request.form["Password"]
        if uname == "admin" and passw == "admin":
            return render_template('home.html',uname=uname)
        else :
             error = "Invalid id or password"
             return render_template('index.html',error=error)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
