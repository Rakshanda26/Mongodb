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
print(db)

database = client['myinfo']
collection = database["Radha"]

record = collection.find()
#for i in record:
    #print(i)


data = collection.find({"company_name" : "Govinda"})

# gt is greater than
data2 = collection.find({"courseOffered" : {"$gt" : "E"}})
for i in data2:
    print(i)


