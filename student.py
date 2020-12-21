from flask import Flask, render_template, request, redirect, Blueprint
from flask_mysqldb import MySQL
from mysql import database

student = Blueprint('student', __name__, template_folder='templates')

@student.route("/HomePage/student", methods = ['GET', 'POST'])
def studentPage():
    if request.method == "POST":
        info = request.form
        choice = info['choice']
        if choice == 'exam' or choice == 'total-grade' or choice == 'review' or choice == 'view-ans' or choice == "view-paper" or choice == "exam-grade":
            questions = [("What is C++", "Language", "CCC", "Other"), ("What is Titanic", "HH Ship", "Italy Ship")]
            questions = getData()
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

def getData():
    cur = database.mysql.connection.cursor()
    cur.execute("SELECT code, Fname, Lname, gender FROM employee")
    data = cur.fetchall()
    database.mysql.connection.commit()
    cur.close()
    return data




