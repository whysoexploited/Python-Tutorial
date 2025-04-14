import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="02121991b",
  database="mydatabase"
)


mycursor = mydb.cursor()

mycursor.execute("""
CREATE TABLE IF NOT EXISTS products (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255)
)
""")

mycursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255),
    fav INT,
    FOREIGN KEY (fav) REFERENCES products(id)
)
""")
users = [
    (1, 'John', 1),
    (2, 'Peter', 1),
    (3, 'Amy', 2),
    (4, 'Hannah', None),
    (5, 'Michael', None)
]

mycursor.executemany("REPLACE INTO users (id, name, fav) VALUES (%s, %s, %s)", users)
mydb.commit()

products = [
  (154, 'Chocolate Heaven'),
  (155, 'Tasty Lemons'),
  (3, 'Vanilla Dreams')  # this one can be anything
]

mycursor.executemany("REPLACE INTO products (id, name) VALUES (%s, %s)", products)
mydb.commit()

print("Users and products sucessfuly created")

sql = "SELECT \
  users.name AS user, \
  products.name AS favorite \
  FROM users \
  RIGHT JOIN products ON users.fav = products.id"

mycursor.execute(sql)

myresult = mycursor.fetchall()

for x in myresult:
  print(x)
