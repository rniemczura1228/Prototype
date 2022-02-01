def get_database():
# Connect to database
    from pymongo import MongoClient
    import pymongo

    # Provide the mongodb atlas url to connect python to mongodb using pymongo
    CONNECTION_STRING = "mongodb+srv://rniemczura1228:3GChildren@cluster0.st0wr.mongodb.net"

    # Create a connection using MongoClient. You can import MongoClient or use pymongo.MongoClient
    from pymongo import MongoClient
    client = MongoClient(CONNECTION_STRING)

    # Create the database for our example (we will use the same database throughout the tutorial
    return client['employee_db']
    
# This is added so that many files can reuse the function get_database()
if __name__ == "__main__":    
    
    # Get the database
    dbname = get_database()

# Insert Data
    collection_name = dbname["employee"]
    from datetime import datetime
    add_date = datetime.now()
    chg_date = add_date

    employee_1 = {
    "_id" : "emp00001",
    "first" : "Raymond",
    "last" : "Niemczura",
    "gender" : "Male",
    "location" : "Phoenixville",
    "email" : "rniemczura1228@gmail.com",
    "add_date" : add_date,
    "change_date" : chg_date
    }

    employee_2 = {
    "_id" : "emp00002",
    "first" : "Rosemary",
    "last" : "Russell",
    "gender" : "Female",
    "location" : "Phoenixville",
    "email" : "roserussell1016@gmail.com",
    "add_date" : add_date,
    "change_date" : chg_date
    }
    collection_name.insert_many([employee_1,employee_2])

    add_date = datetime.now()
    chg_date = add_date
    employee_3 = {
    "_id" : "emp00003",
    "first" : "Heather",
    "last" : "Mahalik",
    "gender" : "Female",
    "location" : "Chester Springs",
    "email" : "hmahalik@gmail.com",
    "add_date" : add_date,
    "change_date" : chg_date
    }
    collection_name.insert_one(employee_3)