def rec(value):
    x = 0
    if(value > 0):
        x = value + rec(value-1)
        print(x)
    else :
        x = 0
    return x

rec(3)
