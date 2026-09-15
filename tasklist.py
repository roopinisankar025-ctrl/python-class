print ("all element using for loop ")

n=[10,20,30,40,50]
for i in n:
    print(i)  

print ("even number") 

n=[10,20,30,40,50]
for i in n :
    if i%2==0:
        print(i)

print ("odd number  ")

n=[3,5,7,9,8]
for i in n:
    if i%2==1:
        print(i)

print(" sum of all number")

n=[10,20,30,40,50]
sum=1
for i in n:
    sum+=i
    print(sum)

print("the largest number using loop ")

n=[10,20,30,40,50]
lar=n[0]
for i in n:
    if i> lar:
        lar=i
print(lar) 

print("the smallest number using loop")

n=[10,20,30,40,50]
sma=n[0]
for i in n:
    if i< sma:
        sma=i
print(sma)

print("count how many positive number")

n=[10,20,-30,40,-50]
count=0
for i in n:
    if i>0:
        count+=1    
print(count)

print("count how many negative number")

n=[10,20,-30,40,-50]
count=0
for i in n:
    if i<0:
        count+=1    
print(count)

print("reverse")
n=[10,20,30,40,50]
for i in reversed(n):
    print(i)

print("count even ,odd")
n=[1,2,3,4,5,6,7,8,9,10]
even=0
odd=0
for i in n:
    if i%2==0:
        even+=1
    else :
        odd+=1
print("even numbers :",even)
print("odd numbers:",odd)