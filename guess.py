import random
secret_num=random.randint(1,50)
attempts=0
while True:
    guess=int(input("enter your guess:"))
    attempts=attempts+1
    if guess < secret_num:
        print("too lowl!")
    elif guess > secret_num:
        print("too high!")
    else:
        print("correct")
        print("you guessed the no in",attempts,"attempts")
        break