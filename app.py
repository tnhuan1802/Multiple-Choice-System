from flask import Flask, render_template, request, redirect
from flask_mysqldb import MySQL
from student import student
app = Flask(__name__)


app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'trannguyen121223'
app.config['MYSQL_DB'] = 'fabric_database'

mysql = MySQL(app)

@app.route("/HomePage", methods = ['GET', 'POST'])
def loggin():
    if request.method == "POST":
        app.register_blueprint(student)
        # info = request.form
        # userName = info['uname']
        # password = info['psw']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO employee VALUES (%s, %s, %s, %s, %s, %s)", ('TH0006969', 'Tran', 'Huan', 'Other', '158, Ly Thuong Kiet, Quan 10, Ho Chi Minh', '01234567891'))
        mysql.connection.commit()
        cur.close()
        return redirect('/HomePage/student')
    return render_template('login.html')


if __name__ == "__main__":
    app.run()