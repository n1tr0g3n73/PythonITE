import math
def eq_1_2(*key):
    if(len(key)==2):
        print("this is a first degree operrion")
        a = int(input("enter the value of a : "))
        b = int(input("enter the value of b : "))
        def equation(a,b):
            if a != 0 :
                print("solution", -b/a)
            else:
                print("devison by zero")
    elif(len(key)==3):
        print("this is a second degree equation")
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
    

