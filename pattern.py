# dec triangle
'''
for i in range (3,0,-1):
    print("*"*i)
#number pattern

for i in range(1,4):
    print(i)
#same number pattern
for i in range(1,4):
    print("1"*i)
#number triange

for i in range(1,4):
    for j in range(1,i+1):
        print(j,end=" ")
    print()
#reverse number paTTERN

for i in range (3,0,-1):
    print(i)
#star line

for i in range(5):
    print("*",end=" ")
#small pyramid

for i in range(1,4):
    print(" "*(3-i)+"* " *i)
# v pattern 

print("*   *")
print(" * * ")
print("  *  ")
#diamond pattern 

n=int(input("enter a value:"))
for i in range(1,n+1):
    for j in range(n-i):
        print(" ",end=" ")
    for j in range(2*i-1):
        print("*",end=" ")
    print()
for i in range(n-1,0,-1):
    for j in range(n-i):
        print(" ",end=" ")
    for j in range(2*i-1):
        print("*",end=" ")
    print()

n=int(input("enter a value:"))
for i in range(1,n+1):
    for j in range(n-i):
        print(" ",end=" ")
    for j in range(2*i-1):
        print("*",end=" ")
    print()'''
n=int(input("enter a value:"))
for i in range(n-1,0,-1):
    for j in range(n-i):
        print(" ",end=" ")
    for j in range(2*i-1):
        print("*",end=" ")
    print()