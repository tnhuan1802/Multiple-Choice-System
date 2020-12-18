from flask import Flask, render_template, request, redirect, Blueprint
from flask_mysqldb import MySQL

student = Blueprint('student', __name__, template_folder='templates')

def func():
    return redirect('/HomePage')

@student.route("/HomePage/student", methods = ['GET', 'POST'])
def studentPage():
    if request.method == "POST":
        info = request.form
        choice = info['choice']
        return render_template('student.html', func= func, choice = choice)
    return render_template('student.html', func = func)


