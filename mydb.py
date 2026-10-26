from pymongo import MongoClient
from bson import ObjectId
myurl=MongoClient("mongodb+srv://roopini2825:roobs2825@cluster0.dgfqvx4.mongodb.net/")
mydb=myurl["roobs-db"]
collection= mydb["user"]
userdata={
    "name":"roopini",
    "mobileno":24356733224,
    "email":"roobs12345@gmail.com",
    "ispass":True,
    "score":590
}
def createuser(user):
    data= collection.insert_one(user)
    print("data added successfully...")
#createuser(userdata)

studentsData = [
    {
    "name": "ArunKumar",
    "mobileno": 9876543210,
    "email": "arun@example.com",
    "ispass": True,
    "score": 590
    },
    {"name": "Priya",
    "mobileno": 9123456780,
    "email": "priya@example.com",
    "ispass": False,
    "score": 450
    },
    {
        "name": "Kumar",
        "mobileno": 9876543212,
        "email": "kumar@example.com",
        "ispass": False,
        "score": 450
    },
    {
        "name": "Divya",
        "mobileno": 9876543213,
        "email": "divya@example.com",
        "ispass": True,
        "score": 920
    },
    {
        "name": "Rahul",
        "mobileno": 9876543214,
        "email": "rahul@example.com",
        "ispass": False,
        "score": 380
    }
]

def MultipleData(students):
    data = collection.insert_many(students)
    print("stduents record created successfully...")
#MultipleData(studentsData)

def getalluser():
    data=collection.find()
    for i in data:
        print(i)
# getalluser()

def getspecificuser(user):
    data=collection.find({"_id":ObjectId(user)})
    for i in data:
        print(i)
# getspecificuser("6ada054956f52d4fa57da3da")

def getdeleteuser(user):
    data=collection.find_one_and_delete({"_id":ObjectId(user)})
    print(data)
    print("for reference deleted successfully")
# getdeleteuser("6ada054956f52d4fa57da3da")


def equality():
    result = collection.find({"score": {"$eq": 450}})
    for data in result:
        print(data)
#equality()
def less_equal():
    result = collection.find({"score": {"$lte": 450}})
    for data in result:
        print(data)
#less_equal()
def greater_equal():
    result = collection.find({"score": {"$gte": 920}})
    for data in result:
        print(data)
#greater_equal()
def not_equal():
    result = collection.find({"score": {"$ne": 1000}})
    for data in result:
        print(data)
#not_equal()
