import pymongo

# Get the database using the method we defined in pymongo_test_insert file 
from pymongo_create_insert_emp import get_database
dbname = get_database()

# Create a new collection
collection_name = dbname["employee"]

item_details = collection_name.find()
print (' Before Change - _id - first - last - gender - location - email - add date - change date') 
for item in item_details:
    print(item['_id'], item['first'], item['last'], item['gender'], item['location'], item['email'], item['add_date'], item['change_date'])

# Query to be updated
query = { "location": "Chester Springs" }
  
# New value
newvalue = { "$set": { "location": "Kimberton" } }
  
# Update the value
collection_name.update_many(query, newvalue)

item_details = collection_name.find()
print (' After Change - _id - first - last - gender - location - email - add date - change date') 
for item in item_details:
    print(item['_id'], item['first'], item['last'], item['gender'], item['location'], item['email'], item['add_date'], item['change_date'])