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

data = {
    'name': 'Raksha',
    'email': 'Raksha@gmail.com',
    'age': 24,
    'subject': ["data_science", "ML", "big_dta"]
}

database = client['myinfo']   # created database
# collection is table inside database - collection multiple documents
# inside myinfo database created table Radha
collection = database["Radha"]
collection.insert_one(data)


