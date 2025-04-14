import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="02121991b",
  database="mydatabase"
)

mycursor = mydb.cursor()

sql = "DROP TABLE IF EXISTS customers"

mycursor.execute(sql)
