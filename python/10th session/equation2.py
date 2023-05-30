import math
def equation(a,b,c):
    y=b**2-4*a*c
    if y==0:
        print("solution",-b/2*a)
    elif y > 0:
        print("solution is",(-b-(math.sqrt(y))/(2*a)))
        print("or",(-b+(math.sqrt(y)/2*a)))
    else :
        print("there is no solution")
equation(2,4,0)
equation(5,10,25)
equation(3,6,3)