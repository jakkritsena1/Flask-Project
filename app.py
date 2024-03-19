from flask import Flask, render_template
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
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
