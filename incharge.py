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
    q1 = Question('1', 'This is question 1',['A','B','C'])
    q2 = Question('2', 'This is question 2',['A','B','C'])
    listQuestion = [['1', 'This is question 1',['A','B','C']]]
    print(listQuestion)
    return render_template('/incharge/question.html', listQuestion = listQuestion)


