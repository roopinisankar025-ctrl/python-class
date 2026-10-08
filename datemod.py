'''from datetime import datetime,date,timedelta

now() current date and time
print(datetime.now())

today() current date
print(date.today())

To get specific part
now = datetime.now()
print(now.year)
print(now.month)
print(now.day)

print(now.hour,"hour")
print(now.minute,"min")
print(now.second,"sec")

#create you own date

date1 = date(2005,7,8)
print(date1)

print(now.strftime("%d-%m-%Y"))
print(now.strftime("%H:%M:%S"))

#Date Difference:
date1 = date(2026,10,12)
date2 = date(2026,10,1)
difference = date1 - date2
print(difference)

time
print(now.time())

timedelta - difference between year / date /time

today = date.today()

tomorrow = today + timedelta(days =10)
yesterday = today - timedelta(days =10,seconds=15,minutes=30,hours=2,weeks=3)
print(tomorrow)
print(yesterday)
'''

# from datetime import datetime,date 
# #def (age):

#     date1=date(2008,11,25)
#     date2=date(2026,11,25)
#     current_age= date2.year -date1.year
#     print(current_age)

from datetime import date

def days_lived(birth):
    today = date.today()
    return (today - birth).days
day = int(input("Enter birth day: "))
month = int(input("Enter birth month: "))
year = int(input("Enter birth year: "))
birth = date(year, month, day)
print("Days lived:", days_lived(birth))

# from datetime import date

# def calculate_age(date1,date2):
#     return date1.year-date2.year
# date1=date(2026,10,5)
# date2=date(2008,11,25)
# difference=date1.year-date2.year
# print(difference)
    