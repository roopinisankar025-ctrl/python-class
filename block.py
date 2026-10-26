try:
    a=20
    b=0
    print(a//b)
except ValueError:
    print("valueerror is executed....")
except ZeroDivisionError:
    print("ZeroDivisionError output is achieved....")
else:
    print("else block executing....")
finally:
    print("execution completed........")
print("--------------------------------------------------")
#
try:
    numbers=[10,20,30,40,50]
    index=5
    print(numbers[index])
except IndexError:
    print("invalid index")
finally:
    print("executed successfully")
print("-----------------------------------------------")

try:
    marks={"ravi":80,
           "priya":95}
    print(marks["arun"])
except KeyError:
    print("student not found")
finally:
    print("executed successfully")
print("-----------------------------------------------")
#
try:
    file=open("data.txt","r")
    print(file.read())
    file.close()
except FileNotFoundError:
    print("check your file name correctly")
finally:
    print("executed successfully")
print("-----------------------------------------------")
#
try:
    a="hello" 
    b=0
    print(int(a)/b)
except ValueError:
    print("invalid number")
except ZeroDivisionError:
    print("can't divide by zero")
finally:
    print("executed successfully")
print("-----------------------------------------------")
#

try:
    age = 18
    if age < 0:
        print("Age cannot be negative!")
    else:
        print("Age:", age)
except ValueError:
    print("Enter a valid integer!")
else:
    print("Age input processed.")
finally:
    print("Age validation completed.")
print("-----------------------------------------------")
#
try:
    marks =90
    if marks < 0 or marks > 100:
        print("Marks must be between 0 and 100!")
    else:
        print("Marks:", marks)
except ValueError:
    print("Enter valid integer marks!")
else:
    print("Marks input processed.")
finally:
    print("Marks validation completed.")
print("-----------------------------------------------")
#

try:
    balance = 5000
    amount=1000
    if amount <= 0:
        print("Enter a valid amount!")
    elif amount > balance:
        print("Insufficient balance!")
    else:
        balance = balance - amount
        print("Withdrawal successful!")
        print("Remaining balance:", balance)
except ValueError:
    print("Enter a valid integer!")
else:
    print("Transaction processed.")
finally:
    print("Transaction completed.")
print("-----------------------------------------------")
# #
# def decorator(func):
#         def wrapper():
#         print("before calling an function")
#         func()
#         print("after calling the function")
#     return wrapper
# @decorator
# def greet():
#     print("hello!")
# greet()


