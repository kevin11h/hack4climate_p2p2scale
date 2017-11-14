from pymongo import MongoClient

DB_NAME = 'p2pscale'  
DB_HOST = 'ds261745.mlab.com'
DB_PORT = 61745
DB_USER = 'test' 
DB_PASS = '123456'

connection = MongoClient(DB_HOST, DB_PORT)
db = connection[DB_NAME]
db.authenticate(DB_USER, DB_PASS)

SEED_DATA = [
    {
        'decade': '1970s',
        'artist': 'Debby Boone',
        'song': 'You Light Up My Life',
        'weeksAtOne': 10
    },
    {
        'decade': '1980s',
        'artist': 'Olivia Newton-John',
        'song': 'Physical',
        'weeksAtOne': 10
    },
    {
        'decade': '1990s',
        'artist': 'Mariah Carey',
        'song': 'One Sweet Day',
        'weeksAtOne': 16
    }
]
# connect to the students database and the ctec121 collection


user_data = {"name":"derta", "age":11}
result = db.users.insert_one(user_data)
print(result.inserted_id)

users = db.users.find()
print('\n All data from users Database \n')
for user in users:
    print(user)

