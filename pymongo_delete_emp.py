import pymongo

# Get the database using the method we defined in pymongo_create_insert_emp 
from pymongo_create_insert_emp import get_database
dbname = get_database()

# Additional comment line
# Create a new collection
collection_name = dbname["employee"]

item_details = collection_name.find()
print (' Before Delete - _id - first - last - gender - location - email - add date - change date') 
for item in item_details:
    print(item['_id'], item['first'], item['last'], item['gender'], item['location'], item['email'], item['add_date'], item['change_date'])

# Delete one item from collection
myquery = {"gender": "Male"}
collection_name.delete_one(myquery)

item_details = collection_name.find()
print ('Hi')
print (' After Delete - _id - first - last - gender - location - email - add date - change date') 
for item in item_details:
    print(item['_id'], item['first'], item['last'], item['gender'], item['location'], item['email'], item['add_date'], item['change_date'])
