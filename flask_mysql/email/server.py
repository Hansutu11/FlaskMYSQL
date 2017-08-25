from flask import Flask, request, render_template, redirect
from mysqlconnection import MySQLConnector
app = Flask(__name__)
mysql = MySQLConnector(app, 'emails')
print mysql.query_db("SELECT * FROM users")
@app.route('/')
def index():
    return render_template('index.html')
@app.route('/sucess', methods=['POST'])
def create():
    return render_template('sucess.html')
app.run(debug=True)
