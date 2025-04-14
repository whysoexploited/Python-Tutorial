import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="02121991b",
    database="mydatabase"
)

mycursor = mydb.cursor()

# CREATE DB AND TABLE IF NOT EXISTS
mycursor.execute("CREATE DATABASE IF NOT EXISTS mydatabase")
mycursor.execute("CREATE TABLE IF NOT EXISTS customers (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), address VARCHAR(255))")
#mycursor.execute("ALTER TABLE IF NOT EXISTS customers ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY") #IF TABLE EXISTS USE THE ALTER TABLE

#SHOW DATABASE
mycursor.execute("SHOW DATABASES")
print("Databases:")
for x in mycursor:
    print(" -", x)

mycursor.execute("SHOW TABLES")
for x in mycursor:
    print(" -", x)

