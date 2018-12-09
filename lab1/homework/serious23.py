from pymongo import MongoClient

#1. Connect to database server
uri = "mongodb://admin:admin@ds021182.mlab.com:21182/c4e"
client = MongoClient(uri)

#2. Select database
db = client.get_database()

#3. Select collection
post = db["posts"]

#4. Create document
new_post = {
    "title": "Why is Lorem Ipsum?",
    "author": "lethanhtrung",
    "content": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nam efficitur et augue sit amet faucibus. Mauris nec magna ligula. Ut nec odio vitae justo ornare maximus in nec nulla. Curabitur faucibus cursus est ut luctus. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam pharetra mauris at justo suscipit, et laoreet massa consequat. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos. Ut faucibus nibh elit, in iaculis neque dapibus eu.",
}

#5. Add document into collection
post.insert_one(new_post)

# 6. Close connection
client.close()
