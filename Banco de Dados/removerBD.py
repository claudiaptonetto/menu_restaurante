import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="python"  
)



mycursor = mydb.cursor()

sql = "DROP DATABASE RESTAURANTE"

mycursor.execute(sql)
