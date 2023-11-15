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

d = {
    "name":"sudhanshu",
    "email" : "sudhanshu@ineuron.ai",
    "surname" : "kumar"
}
d = {
    "name":"sudhanshu",
    "email" : "sudhanshu@ineuron.ai",
    "surname" : "kumar"
}
d = {
    "name":"sudhanshu",
    "email" : "sudhanshu@ineuron.ai",
    "surname" : "kumar"
}
d = {
    "name":"sudhanshu",
    "email" : "sudhanshu@ineuron.ai",
    "surname" : "kumar"
}
d = {
    "name":"sudhanshu",
    "email" : "sudhanshu@ineuron.ai",
    "surname" : "kumar"
}
d = {
    "name":"sudhanshu",
    "email" : "sudhanshu@ineuron.ai",
    "surname" : "kumar"
}

db1 = client['mongotest']
coll = db1['test']
coll.insert_one(d )