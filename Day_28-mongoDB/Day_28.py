################################## Day 28: 69 Days of Python #####################################

# Python MongoDB

# MongoDB stores data in JSON-like documents, which makes the database very flexible and scalable.

# To be able to experiment with the code examples in this tutorial, you will need access to a MongoDB database.

# You can download a free MongoDB database at https://www.mongodb.com.

# Or get started right away with a MongoDB cloud service at https://www.mongodb.com/cloud/atlas.

# PyMongo

# PyMongo is a Python driver for MongoDB.
# It allows you to interact with MongoDB databases from Python.
# You can install PyMongo using pip:
# pip install pymongo

# Creating a Database
# To create a database in MongoDB, start by creating a MongoClient object, then specify a connection URL with the correct ip address and the name of the database you want to create.

# MongoDB will create the database if it does not exist, and make a connection to it.

# Create a database called "mydatabase":

import pymongo

# 1. Get Started
# Connect to MongoDB
client = pymongo.MongoClient("mongodb://localhost:27017/")
print("Connected to MongoDB!")

# 2. Create Database
db = client["mydatabase"]
print("Database created: 'mydatabase'")

# 3. Collection
collection = db["mycollection"]
print("Collection created: 'mycollection'")

# 4. Insert
# Insert one document
data = {"name": "Alice", "age": 25, "city": "New York"}
collection.insert_one(data)
print("Inserted one document.")

# Insert many documents
data_list = [
    {"name": "Bob", "age": 30, "city": "Los Angeles"},
    {"name": "Charlie", "age": 35, "city": "Chicago"}
]
collection.insert_many(data_list)
print("Inserted multiple documents.")

# 5. Find
# Find one document
print("Find one:", collection.find_one())

# Find all documents
print("Find all:")
for doc in collection.find():
    print(doc)

# 6. Query
# Query with a filter
query = {"age": {"$gt": 28}}
print("Query with filter:")
for doc in collection.find(query):
    print(doc)

# 7. Sort
# Sort results by age in descending order
print("Sorted results by age (desc):")
for doc in collection.find().sort("age", -1):
    print(doc)

# 8. Delete
# Delete one document
delete_query = {"name": "Alice"}
collection.delete_one(delete_query)
print("Deleted one document.")

# Delete many documents
delete_many_query = {"age": {"$gte": 30}}
result = collection.delete_many(delete_many_query)
print(f"Deleted {result.deleted_count} documents.")

# 9. Drop Collection
collection.drop()
print("Collection dropped.")

# 10. Update
# Recreate and insert data
collection = db["mycollection"]
collection.insert_one({"name": "Alice", "age": 25, "city": "New York"})
update_query = {"name": "Alice"}
new_values = {"$set": {"city": "San Francisco"}}
collection.update_one(update_query, new_values)
print("Document updated.")

# 11. Limit
# Insert more data for demonstration
collection.insert_many([
    {"name": "Eve", "age": 22, "city": "Boston"},
    {"name": "Frank", "age": 28, "city": "Seattle"}
])
print("Limited results:")
for doc in collection.find().limit(2):
    print(doc)

''' Next topic: Create a REST API ---> Day_29.py '''