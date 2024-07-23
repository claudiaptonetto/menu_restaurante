import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="python",
  database="RESTAURANTE"
)

mycursor = mydb.cursor()

mycursor.execute("INSERT INTO menu (classificacao) VALUES ('Bebida sem Alcool')")
mycursor.execute("INSERT INTO menu (classificacao) VALUES ('Bebida com Alcool')")
mycursor.execute("INSERT INTO menu (classificacao) VALUES ('Entrada')")
mycursor.execute("INSERT INTO menu (classificacao) VALUES ('Prato principal')")
mycursor.execute("INSERT INTO menu (classificacao) VALUES ('Sobremesa')")
mycursor.execute("INSERT INTO Produtos (nome, detalhes, menu, preco) VALUES ('Coca-Cola normal', 'Refrigerante normal', 1, 2.00 )")
mycursor.execute("INSERT INTO Produtos (nome, detalhes, menu, preco) VALUES ('Vinho Tinto', 'Vinho tinto nacional serra gaucha, taça', 2, 12.00 )")
mycursor.execute("INSERT INTO Produtos (nome, detalhes, menu, preco) VALUES ('Suco Uva', 'Suco de uva Integral, Jarra', 1, 20.00 )")
mycursor.execute("INSERT INTO Produtos (nome, detalhes, menu, preco) VALUES ('Suco de Morango', 'Suco de Morango integral, Jarra', 1, 20.00 )")
mycursor.execute("INSERT INTO Produtos (nome, detalhes, menu, preco) VALUES ('Bolinho de peixe', 'Bolinho de peixe frito com farinha de trigo, 6 unidades', 3, 30.00 )")
mycursor.execute("INSERT INTO Produtos (nome, detalhes, menu, preco) VALUES ('Bife a cavalo', 'Bife 500gramas, ovo e fritas', 4, 45.00 )")
mycursor.execute("INSERT INTO Produtos (nome, detalhes, menu, preco) VALUES ('Pizza', 'Calabreza, mussarela e tomate', 4, 35.00 )")

mydb.commit()

print(mycursor.rowcount, "Registro inserido")
