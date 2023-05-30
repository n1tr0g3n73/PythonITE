a= float(input("enter the value of a: \n"))
b= float(input("enter the value of b: \n"))
c = input("enter the desired operation: \n")

if(c == "/"):
    if( b == 0):
        print("error division by zero")
    else:
        print(a / b)
elif(c == "//"):
    if( b == 0):
        print("error division by zero")
    else:
        print(a // b)
elif(c == "%"):
    if( b == 0):
        print("error division by zero")
    else:
        print(a % b)
elif(c == "+"):
    print(a + b)
elif(c == "*"):
    print(a * b)
elif(c == "-"):
    print(a - b)
elif(c == "**"):
    print(a ** b)
else:
    print("you did not enter a math operation,try again")