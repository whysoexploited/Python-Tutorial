import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="02121991b",
    database="mydatabase"
)

mycursor = mydb.cursor()
mycursor.execute("SELECT * FROM customers")
myresult = mycursor.fetchall()

for x in myresult:
    print(x)

mycursor.execute("SELECT name, address FROM customers")

myresult = mycursor.fetchall()

for x in myresult:
    print("- ", x)

mycursor.execute("SELECT * FROM customers")

myresult = mycursor.fetchone()

print(myresult)
