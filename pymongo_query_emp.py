# Get the database using the method we defined in pymongo_create_insert_emp import
from pymongo_create_insert_emp import get_database
dbname = get_database()

# Create a new collection
collection_name = dbname["employee"]

# Print entire collection
item_details = collection_name.find()
print (' All - _id - first - last - gender - location - email - add date - change date') 
for item in item_details:
    print(item['_id'], item['first'], item['last'], item['gender'], item['location'], item['email'], item['add_date'], item['change_date'])

# Print collection where location is Phoenixville
item_details = collection_name.find({"location" : "Phoenixville"})
print (' Phoenixville - _id - first - last - gender - location - email - add date - change date') 
for item in item_details:
    print(item['_id'], item['first'], item['last'], item['gender'], item['location'], item['email'], item['add_date'], item['change_date'])