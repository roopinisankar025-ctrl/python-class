db_name = [
    {
        "name": "roobi",
        "email": "roobi@gmail.com",
        "age": 17,
        "marks": [90, 96, 98, 100, 96],
    },
    {
        "name": "saasha",
        "email": "saasha@gmail.com",
        "age": 17,
        "marks": [88, 79, 98.56, 58],
    },
    {
        "name": "sai",
        "email": "sai@gmail.com",
        "age": 17,
        "marks": [98, 74, 98.86, 48],
    },
    {
        "name": "sharmi",
        "email": "sharmi@gmail.com",
        "age": 17,
        "marks": [98, 29, 98.76, 98],
    },
    {
        "name": "sadhana",
        "email": "sadhana@gmail.com",
        "age": 17,
        "marks": [84, 89, 98, 36, 28],
    },
    {
        "name": "sakthi",
        "email": "sakthi@gmail.com",
        "age": 17,
        "marks": [62, 73, 84, 91, 50],
    },
    {
        "name": "pavithra",
        "email": "pavithra@gmail.com",
        "age": 18,
        "marks": [38, 19, 78, 46, 38],
    },
    {
        "name": "priya",
        "email": "priya@gmail.com",
        "age": 17,
        "marks": [41, 79, 98, 45, 58],
    },
    {
        "name": "hema",
        "email": "hema@gmail.com",
        "age": 17,
        "marks": [88, 46, 98, 32, 58],
    },
    {
        "name": "nivetha",
        "email": "nivetha@gmail.com",
        "age": 19,
        "marks": [14, 79, 68, 56, 98],
    }
]
finallist = []
for i in db_name:
    total = 0
    for j in i["marks"]:
        total += j
    i["total"] = total
rank = 1
while len(db_name) > 0:
    highest = db_name[0]
    for i in db_name:
        if i["total"] > highest["total"]:
            highest = i
    total = highest["total"]
    if total >= 450:
        review = "Outstanding"
    elif total >= 400:
        review = "Excellent"
    elif total >= 350:
        review = "Very Good"
    elif total >= 300:
        review = "Good"
    elif total >= 250:
        review = "Average"
    elif total >= 200:
        review = "Below Average"
    elif total >= 150:
        review = "Poor"
    elif total >= 100:
        review = "Very Poor"
    else:
        review = "Bad"
    finallist.append({
        "name": highest["name"],
        "total_marks": total,
        "rank": rank,
        "review": review 
    })
    rank += 1
    db_name.remove(highest)
for i in finallist:
    print( "Name:", i["name"])
    print(" Total Marks:", i["total_marks"])
    print(" Rank:", i["rank"])
    print(" Review:", i["review"])
    print("------------------------------")
    
    

