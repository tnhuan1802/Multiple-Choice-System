from flask import Flask, render_template, request, redirect, Blueprint
from flask_mysqldb import MySQL
from mysql import database
from user import User
student = Blueprint('student', __name__, template_folder='templates')



@student.route("/index/student", methods = ['GET', 'POST'])
def studentHome():
    questions = anslist = composeID = testcode = questions = choicelist = None
    if request.method == "POST":
        info = request.form
        choice = info['choice']
        if choice == 'exam':
            questions = getExam()
            anslist = questions[1]
            composeID = questions[2]
            testcode = questions[3]
            questions = questions[0]
            choicelist = genAnsList(questions)
            return render_template('student/student.html', choice = choice, questions = questions, choicelist = choicelist, anslist= anslist, name = User.name, id = User.id)
        if choice == 'total-grade' or choice == 'review' or choice == 'view-ans' or choice == "view-paper" or choice == "exam-grade":
            questions = [("What is C++", "Language", "CCC", "Other"), ("What is Titanic", "HH Ship", "Italy Ship")]
            questions = questions
            anslist = genAnsList(questions)
            return render_template('student/student.html', choice = choice, questions = questions, anslist = anslist, name = User.name, id = User.id)
        if choice == 'submission':
            marking(info, anslist, choicelist, testcode, composeID)
            return render_template('student/submission.html')
        return render_template('student/student.html', choice = choice, name = User.name, id = User.id)
    return render_template('student/student.html', name = User.name, id = User.id)

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

def getExam():
    cur = database.mysql.connection.cursor()
    cur.callproc('participateExam', ['Database System', '2020-12-24', '1'])
    data = cur.fetchall()
    cur.close()
    database.mysql.connection.commit()
    q = []
    ans = []
    for i in data:
        if len(q) == 0:
            q.append([i[1]])
        elif q[-1][0] != i[1]:
            q.append([i[1]])
        q[-1].append(i[-3])
        ans.append(i[-2])
    return (q, ans, data[0][-1], '1')

def marking(dict, anslist, choicelist, testcode, composeID):
    grades = 0
    for i in choicelist:
        q_idx = choicelist.index(i)
        if int(dict[i][-1]) == anslist[q_idx]:
            grades = 10/len(anslist)
        cur = database.mysql.connection.cursor()
        cur.execute("INSERT INTO Do Values(%s, %s, %s, %s, %s, %s)", (q_idx, int(dict[i][0], User.id, testcode, composeID, grades)))
        data = cur.fetchall()
        database.mysql.connection.commit()
        cur.close()
        grades = 0
    return data    
    




