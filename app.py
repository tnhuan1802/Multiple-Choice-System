from flask import Flask, render_template, request, redirect
from flask_mysqldb import MySQL
from student import student
from incharge import incharge
from manager import manager
from mysql import database
from user import User
app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'Maestro1802'
app.config['MYSQL_DB'] = 'MyDB'

mysql = MySQL(app)
@app.route("/index", methods = ['GET', 'POST'])
def login():
    if request.method == "POST":
        app.register_blueprint(incharge)
        info = request.form
        userName = info['uname']
        password = info['psw']
        User.username = userName
        User.password = password
        user = checkValidUser(userName, password)
        if len(user) == 0:
            return render_template('login.html', valid = False)
        user = User(user[0][0], user[0][1], user[0][2], user[0][3], userName, password)
        if user.role == 'Student':
            app.register_blueprint(student)
            return redirect('/index/student')
        if user.role == 'Lecturer':
            app.register_blueprint(incharge)
            return redirect('/index/incharge')
        if user.role == 'Manager':
            app.register_blueprint(manager)
            return redirect('/index/manager')
    return render_template('login.html')

def checkValidUser(userName, password):
    cur = database.mysql.connection.cursor()
    cur.execute("SELECT * FROM users WHERE username = %s AND userpassword = %s", (userName, password))
    data = cur.fetchall()
    database.mysql.connection.commit()
    cur.close()
    print(data)
    return data

if __name__ == "__main__":
    app.run()