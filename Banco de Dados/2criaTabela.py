import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="python",
  database="RESTAURANTE"
)


mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE menu (menu_id INT AUTO_INCREMENT PRIMARY KEY, classificacao VARCHAR(40))")
mycursor.execute("CREATE TABLE produtos (produtos_id INT AUTO_INCREMENT PRIMARY KEY, nome VARCHAR(40), detalhes VARCHAR(255), menu INT, preco DOUBLE)")

mycursor.execute("ALTER TABLE produtos ADD FOREIGN KEY(menu) REFERENCES menu(menu_id) ON DELETE SET NULL")
