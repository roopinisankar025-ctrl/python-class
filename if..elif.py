print("multiple")
num=int(input("enter a value:"))
if(num % 3 == 0 and num % 5 == 0 ):
    print("multiples of both 3 and 5")
else:
    print("multiples of not 3 and 5")



print(" password")
password="python125"
key=str(input( "enter a pass:"))
if( key==password):
    print("login successfully")
else:
    print("login failed")



print("----speed checker---")
speed=int(input("enter a value"))
if(speed>100):
    print("over speed")
elif(speed<100 ):
    print('normal speed')
else:
   print(" slow speed")



balance=500
withdrawal=100
if(withdrawal <=0):
    print("invalid amount")
elif(withdrawal>=balance):
    print("insufficient balance")
elif(withdrawal%100 !=0):
    print("enter amount in multiples of 100")
else:
    remaining=balance-withdrawal
    print("withdrawal successfully")
    print("remaining balance:",remaining)

    if remaining <500 :
        print("low balance")

















