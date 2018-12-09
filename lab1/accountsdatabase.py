from pymongo import MongoClient

#1. Connect to database server
uri = "mongodb://admin:admin1@ds229474.mlab.com:29474/c4e24-lab1"
client = MongoClient(uri)

#2. Select database
db = client.get_database()

#3. Select collection
account = db["accounts"]

for account in account.find():  #post_collection.find() la 1 list trong for..in #o ngoai thi khong duoc coi la mot list
    print(account)

# #4. Create document
# new_account = {
#     "username": "thisisaccount3",
#     "email": "lnkln@gmail.com",
#     "phone": 913450102,
#     "yob": "6/9/1999",
#     "password": "lolololo"
# }

# #5. Add document into collection
# account.insert_one(new_account)

#6. Close connection
client.close()

