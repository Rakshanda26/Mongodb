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

# Access a specific database (e.g., 'test')
db = client.test_database  # Replace 'test_database' with your actual database name
collection = db.test_collection  # Replace 'test_collection' with your actual collection name

# Define data to be inserted
data = {
    'name': 'John Doe',
    'email': 'john@example.com',
    'age': 30,
    'status': 'active'
}

# Insert a single document into the collection
result = collection.insert_one(data)

# Print the inserted document's unique ID
print(f"Inserted document ID: {result.inserted_id}")
