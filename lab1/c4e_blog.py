from pymongo import MongoClient

#1. Connect to database server
uri = "mongodb://admin:admin1@ds229474.mlab.com:29474/c4e24-lab1"
client = MongoClient(uri)

#2. Select database
db = client.get_database()

#3. Select collection
post_collection = db["posts"]

for post_collection in post_collection.find():  #post_collection.find() la 1 list trong for..in #o ngoai thi khong duoc coi la mot list
    print(post_collection)

# #4. Create document
# new_document = {
#     "title": "Hôm nay trời đẹp",
#     "post": "Mình ở nhà ngủ",
# }

# #5. Add document into collection
# post_collection.insert_one(new_document)

#6. Close connection
client.close()

