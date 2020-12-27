from flask import Flask, render_template, request, redirect
from flask_mysqldb import MySQL
from student import student
from manager import manager
from mysql import database
from user import User
app = Flask(__name__)


app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'trannguyen121223'
app.config['MYSQL_DB'] = 'fabric_database'

mysql = MySQL(app)
database.mysql = mysql

@app.route("/HomePage", methods = ['GET', 'POST'])
def loggin():
    if request.method == "POST":
        info = request.form
        userName = info['uname']
        password = info['psw']
        user = checkValidUser(userName, password)
        if len(user) == 0:
            return render_template('login.html', valid = False)
        User.name = user[0][0]
        User.age = user[0][1]
        User.role = user[0][2]
        User.id = user[0][3]
        User.username = userName
        User.password = password
        if User.role == 'Student':
            app.register_blueprint(student)
            return redirect('/HomePage/student')
        if User.role == 'Manager':
            app.register_blueprint(manager)
            return redirect('/HomePage/manager')
    return render_template('login.html')

def checkValidUser(userName, password):
    cur = database.mysql.connection.cursor()
    cur.execute("SELECT * FROM users WHERE username = %s AND userpassword = %s", (userName, password))
    data = cur.fetchall()
    database.mysql.connection.commit()
    cur.close()
    return data

if __name__ == "__main__":
    app.run()