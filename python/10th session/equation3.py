import math
a = int(input("enter the value of a : "))
b = int(input("enter the value of b : "))
c = int(input("enterthe value of c : "))
def equation(a,b,c):
    y=(b**2)-(4*a*c)
    if y==0:
        print("solution",-b/(2*a))
    elif y > 0:
        print("solution is",(-b-(math.sqrt(y))/(2*a)))
        print("or",(-b+(math.sqrt(y)/(2*a))))
    else :
        print("there is no solution")
equation(a,b,c)