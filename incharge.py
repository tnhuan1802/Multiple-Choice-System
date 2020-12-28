from flask import Flask, render_template, request, redirect, Blueprint
from flask_mysqldb import MySQL
from mysql import database
from user import User

incharge = Blueprint('incharge', __name__, template_folder='templates')

@incharge.route("/index/incharge", methods = ['GET', 'POST'])
def inChargePage():
    return render_template('/incharge/incharge.html', uname = User.username)


@incharge.route("/index/incharge/question", methods = ['GET', 'POST'])
def questionPage():
    cur = database.mysql.connection.cursor()
    if request.method == "POST":
        
        form = request.form
        if (len(form) == 1):
            qId = int(form['qId'])
            delete_question(qId)
        else:
            subject = form['subject']
            qContent = form['qContent']
            answer_1_type = None
            answer_2_type = None
            answer_3_type = None
            answer_4_type = None
            answer_5_type = None
            try:
                qId_remove = form['qId']
            except:
                pass
            
            try:
                answer_1_type = form['answer-1-type']
            except:
                pass
            try:
                answer_2_type = form['answer-2-type']
            except:
                pass
            try:
                answer_3_type = form['answer-3-type']
            except:
                pass
            try:
                answer_4_type = form['answer-4-type']
            except:
                pass
            try:
                answer_5_type = form['answer-5-type']
            except:
                pass
            answer_1 = (form['answer_1'], 1 if answer_1_type else 0)
            answer_2 = (form['answer_2'], 1 if answer_2_type else 0)
            answer_3 = (form['answer_3'], 1 if answer_3_type else 0)
            answer_4 = (form['answer_4'], 1 if answer_4_type else 0)
            answer_5 = (form['answer_5'], 1 if answer_5_type else 0)
            list_ans = [answer_1,answer_2,answer_3,answer_4,answer_5]
            qId = insert_question(subject, qContent)
            insert_answer(list_ans,qId)
        
    cur.execute("SELECT questionid,question_content FROM question")
    listQuestion = cur.fetchall()
    cur.execute("SELECT questionid,type,answer_content FROM question NATURAL JOIN answer")
    listQuestionWithAns = list(cur.fetchall())
    if len(listQuestion) > 0:
        # print(listQuestionWithAns)
        listAnswer = []
        listAnswerWithSameQid = []
        #ans: (qid, content, type) => [(qid,[(content,type), other ans of same question....]), other type of question ....]
        curQID = listQuestionWithAns[0][0]
        for item in listQuestionWithAns:
            
            if curQID == item[0]:
                listAnswerWithSameQid.append([item[2],item[1]])
            else:
                listAnswer.append((curQID,listAnswerWithSameQid))
                listAnswerWithSameQid = []
                curQID = item[0]
                listAnswerWithSameQid.append([item[2],item[1]])
        curQID = listQuestionWithAns[len(listQuestionWithAns) - 1][0]
        listAnswerWithSameQid = []
        for idx in range(len(listQuestionWithAns)):
            if curQID == listQuestionWithAns[idx][0]:
                listAnswerWithSameQid.append([listQuestionWithAns[idx][2],listQuestionWithAns[idx][1]])
            if idx == len(listQuestionWithAns) - 1:
                listAnswer.append((curQID,listAnswerWithSameQid))
        cur.close()
        finalListQuestion = []
        for q in listQuestion:
            
            for a in listAnswer:
                if q[0] == a[0]:
                    curList = list(q)
                    curList.append(a[1])
                    finalListQuestion.append(curList)
        listQuestion = finalListQuestion    

    database.mysql.connection.commit()
    return render_template('/incharge/question.html', listQuestion = listQuestion)

@incharge.route("/index/incharge/exam", methods = ['GET', 'POST'])
def examPage():
    q1 = ('1', "This is question 1",['A','B','C','D'])
    q2 = ('2', "This is question 2",['A','B','C'])
    listQuestion = [q1,q2]
    listTest = [('001','191','Database System',listQuestion, None),('002','192','Principles Of Programming Language',listQuestion, None)]
    unconfirmedTest = list(filter(lambda x : x[4] == None,listTest))
    role = 1
    if request.method == 'POST':
        form = request.form
        subjectId = form['subject']
        semesterId = form['semesterId']

    return render_template('/incharge/exam.html', listQuestion = listQuestion, unconfirmedTest = unconfirmedTest, listTest = listTest, role = role)

def insert_question(subject, content):
    cur = database.mysql.connection.cursor()
    cur.callproc('insert_question',[subject, content])
    data = cur.fetchall()
    cur.close()
    database.mysql.connection.commit()
    return data[0][0]

def delete_question(qId):
    cur = database.mysql.connection.cursor()
    cur.execute("DELETE FROM question WHERE questionid = %s",(qId,))
    cur.close()
    database.mysql.connection.commit()

def insert_answer(list_ans, qId, ):
    cur = database.mysql.connection.cursor()
    for ans in list_ans:
        if ans[0]:
            cur.execute('INSERT INTO answer(questionid, type, answer_content) VALUES (%s,%s,%s)',(qId, ans[1], ans[0]))
    cur.close()
    database.mysql.connection.commit()            
