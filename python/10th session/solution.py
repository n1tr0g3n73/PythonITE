import math
def choise(*vals):
    if(len(vals)==2):
        first_degree(vals[0],vals[1])
    elif(len(vals)==3):
        second_degree(vals[0],vals[1],vals[2])
    else:
        print("error")
def first_degree(a,b):
    print("the equation is first degree")
    if( a == 0):
        print("there is no solution")
    else:
        print("x = ",(-b)/a)

def second_degree(a,b,c):
    print("second degree equation")
    delta = (b**2)-(4*a*c)
    if(delta == 0):
        print("x = ",(-b)/(2*a))
    elif(delta > 0):
        print("x1 = ",(((-b)-(math.sqrt(delta)))/(2*a)))
        print("x2 = ",(((-b)+(math.sqrt(delta)))/(2*a)))
    else:
        print("there is no solution")
choise(2,4)
choise(2,4,2)
choise(-5,10)
choise(6,5,7,10)    