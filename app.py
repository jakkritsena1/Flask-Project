from flask import Flask, render_template, request
# from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'flask_project'

# mysql = MySQL(app)

@app.route('/', methods=['POST', 'GET'])
def login():
    if request.method == "POST":
        # uname = request.form["User"]
        # passw = request.form["Password"]
        # cur = mysql.connection.cursor()
        # cur.execute("SELECT * FROM users WHERE username = %s AND password = %s", (uname, passw))
        # user = cur.fetchone()
        # cur.close()
        # if user:
        #     return render_template('home.html')
        # else:
        #     error = "Invalid username or password"
            return render_template('home.html')
if __name__ == '__main__':
    app.run(debug=True)
