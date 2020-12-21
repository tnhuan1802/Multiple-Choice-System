from flask import Flask, render_template, request, redirect
from flask_mysqldb import MySQL
from student import student
from incharge import incharge
app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'Maestro1802'
app.config['MYSQL_DB'] = 'MyDB'

mysql = MySQL(app)

@app.route("/HomePage", methods = ['GET', 'POST'])
def login():
    if request.method == "POST":
        app.register_blueprint(student)
        app.register_blueprint(incharge)
        # info = request.form
        # userName = info['uname']
        # password = info['psw']
        return redirect('/HomePage/student')
    return render_template('login.html')


if __name__ == "__main__":
    app.run()