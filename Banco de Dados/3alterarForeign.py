import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="python",
  database="RESTAURANTE"
)


mycursor = mydb.cursor()

mycursor.execute("ALTER TABLE produtos ADD FOREIGN KEY(menu) REFERENCES menu(menu_id) ON DELETE SET NULL")
