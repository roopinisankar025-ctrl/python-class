'''# 1
ispass = int(input("Enter the number: "))
n = bool(ispass)
print(type(n))
match n:
    case True:
        print("pass")
    case False:
        print("fail")

 #2       
num=int(input("enter a num:"))
match(num):
     case 2|4|6|8 :
         print('even')
     case 1|3|5|7|9 :
         print("odd")
     case _ :
         print("default is working")



 #3
n=int(input("enter a num:"))
match(n):
    case (n) if ( n > 0):
        print("positive")
    case (n) if(n< 0):
        print("negative")
    case _ :
        print("zero")


#4
n = int(input("Enter n value: "))
m = int(input("Enter m value: "))
c = input("Enter an operator: ")
match (n, c, m):
    case (n, "+", m):
        print(n + m)
    case (n, "-", m):
        print(n - m)
    case (n, "*", m):
        print(n * m)
    case (n, "/", m):
        print(n / m)
    case _:
        print("Invalid operator")


#5
day=int(input('enter a day :'))
match(day):
        case 1| 2| 3| 4| 5 :
            print("weekday")
        case 6|7:
            print("weekend")
        case _ :
            print("invalid day")


#6
marks = int(input("Enter your marks: "))
match marks:
    case m if  m >= 95 :
       print(" grade A+")
    case m if m >= 90 :
       print("grade A")
    case m if m >= 80:
       print(" gradeB1")
    case m if m >= 70:
       print ("grade b ")
    case m if m >= 60:
       print("grade c")
    case m if m >= 50:
       print(" grade d")
    case _:
       print( "just pass 35 and above below 35 fail  ")

#7       
month = int(input("Enter month number (1-12): "))
match month:
    case 1:
        print("January")
    case 2:
        print("February")
    case 3:
        print("March")
    case 4:
        print("April")
    case 5:
        print("May")
    case 6:
        print("June")
    case 7:
        print("July")
    case 8:
        print("August")
    case 9:
        print("September")
    case 10:
        print("October")
    case 11:
        print("November")
    case 12:
        print("December")
    case _:
        print("Invalid month number")


#8
ch = input("Enter a character: ")
match ch.lower():
    case 'a' | 'e' | 'i' | 'o' | 'u':
        print("Vowel")
    case _:
        print("Consonant")
#9
color = input("Enter traffic signal color: ")
match color :
    case "red":
        print("Stop")
    case "yellow":
        print("Get Ready")
    case "green":
        print("Go")
    case _:
        print("Invalid color")

#10
year = int(input("Enter a year: "))
match year % 4:
    case 0:
        print("Leap Year")
    case _:
        print("Not a Leap Year")

#11
age = int(input("Enter your age: "))
match age:
    case a if  1<= a <=12:
        print("Child")
    case a if 12 <= a <= 20:
        print("Teenage")
    case a if 20 <= a <= 59:
        print("Adult")
    case a if a >= 60:
        print("Senior Citizen")
    case _:
        print("Invalid age")

'''
'''#11(a)
a=int(input("enter a value :"))
match a :
    case 1|2|3|4|5|6|7|8|9|10 :
        print("between 1 to 10 numbers")
    case _ :
        print("below and above the numbers ")

#12
db_name="roopini028"
password="nick2345"
username=input("enter an name :")
userpass=input("enter pass :")
match username,userpass :
    case( m, n) if m == db_name and n == password :
        print( " both username and password is correct")
    case _ :
        print( "both username and password are incorrect ")

#13
shape=int (input("enter your shape number:"))
match shape :
    case 4 :
        print("square, rectangle")
    case 3 :
        print("triangle")
    case _ :
        print("circle")


#14
num1=int(input("enter a value:"))
match num1 :
    case n if n % 3 ==0 and n % 5 == 0 :
        print("both are divisible")
    case _ :
        print("both are not divisible")'''

#15
n=int(input("enter a value:"))
match n :
    case n if n > 0 and n % 2 == 0 :
        print("positive even ")
    case n if n > 0 and n % 2 != 0 :
        print("positive odd")
    case n if n == 0 :
        print("zero")
    case _ :
        print("negative")
        
    





       










