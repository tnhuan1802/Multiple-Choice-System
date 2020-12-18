from flask import Flask, render_template, request, redirect
from flask_mysqldb import MySQL
from student import student
app = Flask(__name__)
#app.register_blueprint(student)

@app.route("/HomePage", methods = ['GET', 'POST'])
def loggin():
    if request.method == "POST":
        app.register_blueprint(student)
        # info = request.form
        # userName = info['uname']
        # password = info['psw']
        return redirect('/HomePage/student')
    return render_template('login.html')


if __name__ == "__main__":
    app.run()