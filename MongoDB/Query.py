import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["customers"]

myquery = { "address": "Park Lane 38"}

mydoc = mycol.find(myquery)

for x in mydoc:
    print(x)

#Find documents that start with the letter S or higher( "$gt" - greater than modifier )

myquery = { "address": { "$gt": "S" } }

mydoc = mycol.find(myquery)

for x in mydoc:
    print(x)

#Regex filter to find documents where address starts with the letter S

myquery = { "address": { "$regex": "^S" } }

mydoc = mycol.find(myquery)

for x in mydoc:
    print(x)

