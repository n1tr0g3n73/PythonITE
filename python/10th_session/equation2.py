import math 

def equation_solution(a,b,c):
    delta = (b**2)-(4*a*c)

    if delta == 0 :
        print("x = ",(-b/(2*a)))
    elif delta > 0:
        print("x1 = ",(-b - (math.sqrt(delta)))/(2*a))
        print("x2 = ",(-b + (math.sqrt(delta)))/(2*a))
    else:
        print("there is no solution")


equation_solution(int(input("enter the value of a")),int(input("enter the value of b")),int(input("enter the value of c")))

