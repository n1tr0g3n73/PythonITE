password = input("enter your password: ")
x = 1
while(password != "123abc" and x<5):
    password = input("incorrect password, try again: ")
    if(password != "123abc"):
        x+=1
if(x==5):
    print("you are out of attempts, try again later")
else:
    print("welcome")