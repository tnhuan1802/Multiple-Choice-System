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
app.config['MYSQL_PASSWORD'] = 'trannguyen121223'
app.config['MYSQL_DB'] = 'mc_database'

mysql = MySQL(app)
database.mysql = mysql
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
            return redirect('/index/incharge')
            # return render_template('login.html', valid = False)
        User.role = user[0][0]
        User.id = user[0][1]
        User.username = userName
        User.password = password
        if User.role == 'Student':
            app.register_blueprint(student)
            return redirect('/index/student')
        if User.role == 'Lecturer':
            app.register_blueprint(incharge)
            return redirect('/index/incharge')
        if User.role == 'Manager':
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