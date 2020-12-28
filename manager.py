from flask import Flask, render_template, request, redirect, Blueprint
from flask_mysqldb import MySQL
from mysql import database

manager = Blueprint('manager', __name__, template_folder='templates')

@manager.route("/index/manager", methods = ['GET', 'POST'])
def managerPage():
    choice = None
    if request.method == 'POST':
        info = request.form
        choice = info['choice']
        if choice == 'view-grade':
            questions = [("What is C++", "Language", "CCC", "Other"), ("What is Titanic", "HH Ship", "Italy Ship")]
            anslist = genAnsList(questions)
            return render_template('manager.html', choice = choice, questions = questions, anslist = anslist)
        if choice == 'process':
            return redirect("/index/manager/process")
    return render_template('manager/manager.html', choice = choice)

@manager.route("/index/manager/process", methods = ['GET', 'POST'])
def process():
    questions = [("What is C++", "Language", "CCC", "Other"), ("What is Titanic", "HH Ship", "Italy Ship")]
    questions = questions*10
    return render_template('manager/process.html', questions = questions)

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