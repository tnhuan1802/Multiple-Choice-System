from flask import Flask, render_template, request, redirect, Blueprint
from flask_mysqldb import MySQL
from mysql import database

manager = Blueprint('manager', __name__, template_folder='templates')

@manager.route("HomePage/manager", method = ['POST'])
def managerPage():
    if request.method == 'POST':
        pass
    return render_template('manager.html')

    