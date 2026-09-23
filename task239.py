print ("all element using for loop ")
n=[2,4,6,7]
def num(i):
    for i in n:
        print(i)  
num(n)

print ("even number") 
n=[2,4,3,7]
def even(i):
    for i in n:
        if i%2==0:
            print(i)
even(n)

print ("odd number  ")
n=[2,3,5,7,4]
def odd(i):  
    for i in n:
     if i%2==1:
        print(i)
odd(n)

print('check number')
n=4
def positive(m):
    if(m==0):
      print('zero')
    elif(m>0):
      print('positive')
    else:
      print('negative')
positive(n)

print("the greatest three num")
x=8
y=48
z=24
def greatest(a,b,c):
    if(a>=b):
        print("a is greater than b")
    elif(b>=c):
        print("b is greater than c")
    else:
        print("c is not greater than a,b ")
greatest(x,y,z)

print ("even number") 
n=[10,20,30,40,50]
def even(i): 
    count=0
    for i in n :
        if i%2==0:
            count+=1
    print(count)
even(n)


print ("odd number  ")
n=[3,5,4,9,8]
def neg(i):
    for i in n:
        if i%2==1:
             print(i)
neg(n)

print("sum of all number")
n=[1,2,4,6]
def num(i):
    sum=0
    for i in n:
         sum+=i
    print(sum)
num(n)
