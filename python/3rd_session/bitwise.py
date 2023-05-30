"""
it's a python script to
demonstrate bitwise
operations 
"""
a = 2
b = 4
#print a in binary 

print(bin(a))
#print b in binary
print(bin(b))
#print a & b in binary
print("a and b",bin(a & b),"\n")
#print a | b in binary
print("a or b",bin(a | b),"\n")
#print ~a in binary
print("not a",bin(~a),"\n")
print("a xor b",bin(a ^ b),"\n")
print("right shift a by 2",bin(a >> 2),"\n")
print("left shift a by 2",bin(a << 2),"\n")

#using bitwise operators in decimal
print("a and b",a & b,"\n")
print("a or b",a | b,"\n")
print("not a",~a,"\n")
print("a xor b",a ^ b,"\n")
print("left shift a by 2",a >> 2,"\n")
print("left shift a by 2",a << 2,"\n")