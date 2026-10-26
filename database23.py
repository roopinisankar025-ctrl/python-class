def equality():
    result = collection.find({"price": {"$eq": 100}})
    for data in result:
        print(data)
#
def less_equal():
    result = collection.find({"price": {"$lte": 100}})
    for data in result:
        print(data)
#
def greater_equal():
    result = collection.find({"price": {"$gte": 100}})
    for data in result:
        print(data)
#
def not_equal():
    result = collection.find({"price": {"$ne": 100}})
    for data in result:
        print(data)