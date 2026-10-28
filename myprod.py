from pymongo import MongoClient
from bson import ObjectId
myURL = MongoClient("mongodb+srv://roopini2825:roobs2825@cluster0.dgfqvx4.mongodb.net/")
myDB = myURL["roobs-db"]
myproducts= myDB["product"]
products = [
    {"product_id": 1,
      "name": "Laptop",
        "category": "Electronics", 
        "price": 45000,
        "quantity": 10
    },
    {"product_id": 2,
      "name": "Mobile Phone",
      "category": "Electronics",
      "price": 15000,
      "quantity": 20
    },
    {"product_id": 3,
     "name": "Headphones",
     "category": "Accessories",
     "price": 1200,
     "quantity": 30
    },
    {"product_id": 4,
     "name": "Keyboard", 
     "category": "Accessories", 
     "price": 800, 
     "quantity": 15
    },
    {"product_id": 5,
     "name": "Mouse",
     "category": "Accessories",
     "price": 500, 
     "quantity": 25
    },
    {"product_id": 6, 
     "name": "Monitor", 
     "category": "Electronics", 
     "price": 12000, 
     "quantity": 8
    },
    {"product_id": 7, 
     "name": "Smart Watch", 
     "category": "Wearables", 
     "price": 2500, "quantity": 12
    },
    {"product_id": 8, 
     "name": "Tablet", 
     "category": "Electronics", 
     "price": 18000, 
     "quantity": 7
    },
    {"product_id": 9, 
     "name": "USB Cable", 
     "category": "Accessories", 
     "price": 250, 
     "quantity": 40
    },
    {"product_id": 10, 
     "name": "Printer", 
     "category": "Electronics", 
     "price": 8500, 
     "quantity": 5
    },
    {"product_id": 11, 
     "name": "Power Bank", 
     "category": "Accessories", 
     "price": 1800, 
     "quantity": 18
    }
]
def multidata(item):
    myproducts.insert_many(products)
    print("myproducts data inserted successfully!!!!")
#multidata(products)

def getallproduct():
    data=myproducts.find()
    for i in data:
        print(i)
# getallproduct()

def getspecificproduct(product):
    data=myproducts.find_one({"_id":ObjectId(product)})
    print(data)
#getspecificproduct("6adf33eccb4136c70bda9719")

def getdeleteproduct(product):
    data=myproducts.find_one_and_delete({"_id":ObjectId(product)})
    print(data)
    print("for reference deleted successfully")
# getdeleteproduct("6adf33eccb4136c70bda9719")
def updatepro(product):
    data=myproducts.update_one(
        {"_id":ObjectId(product)},
        {"$set":{"price":2000}}
    )
    print(data.matched_count)
    print(data.modified_count)
    print("update successfully!!!")
# updatepro("6adf3e8df307799946609526")