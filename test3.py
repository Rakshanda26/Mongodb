data =  [
        {
            "item": "canvas",
            "qty": 100,
            "size": {"h": 28, "w": 35.5, "uom": "cm"},
            "status": "A",
        },
        {
            "item": "journal",
            "qty": 25,
            "size": {"h": 14, "w": 21, "uom": "cm"},
            "status": "A",
        },
        {
            "item": "mat",
            "qty": 85,
            "size": {"h": 27.9, "w": 35.5, "uom": "cm"},
            "status": "A",
        },
        {
            "item": "mousepad",
            "qty": 25,
            "size": {"h": 19, "w": 22.85, "uom": "cm"},
            "status": "P",
        },
        {
            "item": "notebook",
            "qty": 50,
            "size": {"h": 8.5, "w": 11, "uom": "in"},
            "status": "P",
        },
        {
            "item": "paper",
            "qty": 100,
            "size": {"h": 8.5, "w": 11, "uom": "in"},
            "status": "D",
        },
        {
            "item": "planner",
            "qty": 75,
            "size": {"h": 22.85, "w": 30, "uom": "cm"},
            "status": "D",
        },
        {
            "item": "postcard",
            "qty": 45,
            "size": {"h": 10, "w": 15.25, "uom": "cm"},
            "status": "A",
        },
        {
            "item": "sketchbook",
            "qty": 80,
            "size": {"h": 14, "w": 21, "uom": "cm"},
            "status": "A",
        },
        {
            "item": "sketch pad",
            "qty": 95,
            "size": {"h": 22.85, "w": 30.5, "uom": "cm"},
            "status": "A",
        },
    ]

import pymongo
from urllib.parse import quote_plus

# MongoDB connection settings
username = "radhhikaraman7979"
password = "rakshanda@26"
cluster_url = "cluster0.awbhqng.mongodb.net"

# URL encode username and password
quoted_username = quote_plus(username)
quoted_password = quote_plus(password)

# Create a new client and connect to the server with encoded credentials
client = pymongo.MongoClient(f"mongodb+srv://{quoted_username}:{quoted_password}@{cluster_url}/test?retryWrites=true&w=majority")

db = client.test
#print(db)
database = client['inventory']
collection = database["table"]
collection.insert_many(data)
d = collection.find()

# STATUS is p or A
d1 = collection.find({"status" : {"$in" : ['A', 'P']}})

# STATUS is greater than c
d2 = collection.find({"status" : {"$gt" : "C"}})

# Quantity is greater than > $gt
# quantity is greater than equal to 100 - $gte
d3 = collection.find({"qty" : {"$gte" : 75}})

# find record where item is sketch pad and qty is 95
d4 = collection.find({"item" : "sketch pad", "qty" : 95})

# find record where item is sketch pad and qty is grater than equal to 75
d5 = collection.find({"item" : "sketch pad", "qty" : {"$gte" : 75}})

# searching below records using OR condintion either one should be true
d5 = collection.find({"$or" : [ {"item" : "sketch pad"} , {"qty" : {"$gte" : 75} } ]  })

# Update the item where we have item = canvas
#collection.update_one({'item': 'canvas'}, {"$set" : {'item': 'Basuri'}})
d6 = collection.find({'item': 'Basuri'})

# Delete the record
collection.delete_one({'item': 'Basuri'})
d7 = collection.find({'item': 'Basuri'})
for i in d7:
    print(i)


