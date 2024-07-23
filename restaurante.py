from flask import Flask, render_template, redirect, request, session, send_file
# The Session instance is not used for direct access, you should always use flask.session
from flask_session import Session
from flask import render_template
from flask import Flask
from flask import request

import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="python",
  database="restaurante"
)

app = Flask(__name__,
            static_url_path='', 
            static_folder='static',
            template_folder='templates')


@app.route("/")
def principal():
    return redirect('index.html')


@app.route("/botao", methods=['GET'])
def pega():
    classificacao = request.args.get('codigo', default = '*', type = str)
    print(classificacao)
    mycursor = mydb.cursor()
    sql = "SELECT * FROM menu WHERE classificacao ='"+classificacao+"' LIMIT 1"
    mycursor.execute(sql)
    myresult = mycursor.fetchall()
    print(myresult)
    return myresult


@app.route("/produtos", methods=['GET'])
def produtos():
    lista = request.args.get('lista', default = '*', type = str)
    mycursor = mydb.cursor()
    sql = "SELECT * FROM produtos WHERE menu = '"+lista+"'"
    mycursor.execute(sql)
    myresult = mycursor.fetchall()
    return myresult


@app.route("/pegaMenu", methods=['GET'])
def pegaMenu():
    mycursor = mydb.cursor()
    sql = "SELECT classificacao FROM menu"
    mycursor.execute(sql)
    myresult = mycursor.fetchall()
    print(myresult)
    return myresult


if __name__ == "__main__":
    app.run(port=4000)