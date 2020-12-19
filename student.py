from flask import Flask, render_template, request, redirect, Blueprint
from flask_mysqldb import MySQL

student = Blueprint('student', __name__, template_folder='templates')


@student.route("/HomePage/student", methods = ['GET', 'POST'])
def studentPage():
    if request.method == "POST":
        info = request.form
        choice = info['choice']
        if choice == 'exam' or choice == 'review':
            questions = [("What is C++", "Language", "CCC", "Other"), ("What is Titanic", "HH Ship", "Italy Ship")]
            # questions = questions*10
            anslist = genAnsList(questions)
            return render_template('student.html', choice = choice, questions = questions, anslist = anslist)
        if choice == 'submission':
            return render_template('submission.html')
        return render_template('student.html', choice = choice)
    return render_template('student.html')

def genAnsList(questions):
    ansl = []
    for i in range(len(questions)):
        ansl.append("Answer" + str(i))
    return ansl




