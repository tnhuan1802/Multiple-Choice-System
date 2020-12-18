from flask import Flask, render_template, request, redirect
from flask_mysqldb import MySQL
from student import student
from incharge import incharge
app = Flask(__name__)
#app.register_blueprint(student)

@app.route("/HomePage", methods = ['GET', 'POST'])
def login():
    if request.method == "POST":
        # app.register_blueprint(student)
        app.register_blueprint(incharge)
        # info = request.form
        # userName = info['uname']
        # password = info['psw']
        return redirect('/HomePage/incharge')
    return render_template('login.html')


if __name__ == "__main__":
    app.run()