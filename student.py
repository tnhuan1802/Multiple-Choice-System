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
        if choice == 'quiz':
            questions = [("What is C++", "Language", "CCC", "Other"), ("What is Titanic", "HH Ship", "Italy Ship")]
            questions = questions*10
            anslist = genAnsList(questions)
            return render_template('student.html', func= func, choice = choice, questions = questions, anslist = anslist)
        if choice == 'submission':
            return '<h1>Correct Answers: <u>'+str(info['Answer1'])+'</u></h1>'
        return render_template('student.html', func= func, choice = choice)
    return render_template('student.html', func = func)

def genAnsList(questions):
    ansl = []
    for i in range(len(questions)):
        ansl.append("Answer" + str(i))
    return ansl




