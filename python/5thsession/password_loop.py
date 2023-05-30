pass_correct = True
i=0

while(i < 5) and (pass_correct):
    password = input("enter your password")
    if(password == "123456789"):
        pass_correct = False
    else:
        i+=1

if(not pass_correct):
    print("welcome")
else:
    print("uv reached the max number of tries")