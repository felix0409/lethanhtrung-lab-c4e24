from pymongo import MongoClient
from matplotlib import pyplot

# Connect to database server
uri = "mongodb://admin:admin@ds021182.mlab.com:21182/c4e"
client = MongoClient(uri)

# Select database
db = client.get_database()

# Select collection
customer = db["customers"]

count1 = 0
count2 = 0
count3 = 0
for i in customer.find():
    if i["ref"].count("events") == 1:
        count1 += 1
    elif i["ref"].count("ads") == 1:
        count2 += 1
    elif i["ref"].count("wom") == 1:
        count3 += 1

refs_counts = [count1, count2, count3]
refs_names = ["events", "ads", "wom"]

pyplot.pie(refs_counts, labels=refs_names, autopct="%.1f%%", shadow=True, explode=[0, 0, 0])
pyplot.title("Marketing references")
pyplot.axis("equal")
pyplot.show()

client.close()
