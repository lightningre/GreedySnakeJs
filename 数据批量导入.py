import pymongo
import os
import string

myclient = pymongo.MongoClient('mongodb://localhost:27017/')
 
dblist = myclient.list_database_names()
if "cet" in dblist:
  print("Database already exists!")

mydb = myclient["cet"]
mycol = mydb["cet4"]


for filename in li:
    mydict = { "name": filename.split(".")[0], "year": "2020", "type": "词汇" }
    x = mycol.insert_one(mydict) 
    print(x.inserted_id)

x = mycol.find_one()
print(x)
