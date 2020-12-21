from flask import Flask, render_template, request, redirect, Blueprint
from flask_mysqldb import MySQL

incharge = Blueprint('incharge', __name__, template_folder='templates')

def func():
    return "Hello"

@incharge.route("/HomePage/incharge", methods = ['GET', 'POST'])
def inChargePage():
    return render_template('incharge.html', func = func)


