from flask import Flask, render_template, request, redirect, Blueprint
from flask_mysqldb import MySQL
from question import Question
from user import User

incharge = Blueprint('incharge', __name__, template_folder='templates')

@incharge.route("/index/incharge", methods = ['GET', 'POST'])
def inChargePage():
    return render_template('/incharge/incharge.html', uname = User.username)


@incharge.route("/index/incharge/question", methods = ['GET', 'POST'])
def questionPage():
    q1 = ('1', "This is question 1",['A','B','C','D'])
    q2 = ('2', "This is question 2",['A','B','C'])
    listQuestion = [q1,q2]
    return render_template('/incharge/question.html', listQuestion = listQuestion)

@incharge.route("/index/incharge/exam", methods = ['GET', 'POST'])
def examPage():
    q1 = ('1', "This is question 1",['A','B','C','D'])
    q2 = ('2', "This is question 2",['A','B','C'])
    listQuestion = [q1,q2]
    role = 1
    return render_template('/incharge/exam.html', listQuestion = listQuestion, role = role)
